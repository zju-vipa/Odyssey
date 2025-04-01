import os
import re
import json
from filelock import FileLock
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from odyssey.prompts import load_prompt
from odyssey.utils.logger import get_logger, Timer
from odyssey.agents.llm import call_with_messages, ModelType

class MemoryManager:
    def __init__(
            self,
            memory_dir=None,
            memory_path=None,
            team_name=None,
            model_type=None,
            dashscope_model=None,
            username=None
        ):
        """
        Initialize the MemoryManager with the required parameters.
        
        :param request_timeout: Timeout for requests (default: 120 seconds)
        :param model_type: Name of the model to use (default: ModelType.LLAMA3_8B)
        :param memory_dir: Directory for storing memory files (default: 'memory')
        :param obs_file_path: Path to the observation JSON file relative to memory_dir
        """
        self.team_name = team_name
        self.username = username
        self.memory_dir = memory_dir
        self.memory_path = memory_path
        self.model_type = model_type
        self.dashscope_model = dashscope_model
        self.logger = get_logger("MC-Multi-Agent")
        self.obs_file_path = f'memory/{self.team_name}/obs/{self.username}.json'

    def render_user_observation(self):
        """
        Render the observation for the specified username from the JSON file.
        
        :return: The observation as a string
        """
        # Check if the file exists
        if not os.path.exists(self.obs_file_path):
            raise FileNotFoundError(f"{self.obs_file_path} not found")
        
        # Read and parse the JSON file
        with open(self.obs_file_path, 'r') as file:
            obs_data = json.load(file)
        
        # Get the value for the given username and convert it to string
        user_observation = str(obs_data)
        return user_observation

    def render_human_message(self, cur_action=None):
        user_message = self.render_user_observation() + "\n Your current action: " + (cur_action if cur_action else "None")
        # Create an instance of HumanMessage with the obtained content
        human_message = HumanMessage(content=user_message)
        return human_message

    def render_system_message(self, goal_str):
        prompt = load_prompt("send_latest_obs")
        system_message = SystemMessage(content=goal_str+prompt)
        return system_message

    def memory_reset(self):
        """Reset memory by ensuring the required directory and files exist and are empty."""
        # Ensure team directory exists
        team_dir = os.path.join(self.memory_dir, self.team_name)
        if not os.path.exists(team_dir):
            os.makedirs(team_dir, exist_ok=True)
            self.logger.success(f"Created team directory: {team_dir}")

        # Ensure obs directory exists
        obs_dir = os.path.join(team_dir, "obs")
        if not os.path.exists(obs_dir):
            os.makedirs(obs_dir, exist_ok=True)
            self.logger.success(f"Created obs directory: {obs_dir}")

        # List of files to reset with their initial content
        files_to_reset = {
            "mem.json": {},
            "chat_log.json": {},
            os.path.join("obs", f"{self.username}.json"): {}
        }

        # Loop through each file and reset it
        for filename, initial_content in files_to_reset.items():
            file_path = os.path.join(team_dir, filename)
            if not os.path.exists(file_path):
                with open(file_path, "w", encoding="utf-8") as file:
                    json.dump(initial_content, file, indent=2)
                self.logger.success(f"Created and initialized file: {file_path}")
            else:
                with open(file_path, "w", encoding="utf-8") as file:
                    json.dump(initial_content, file, indent=2)
                self.logger.success(f"Reset file: {file_path}")

        self.logger.success("Memory reset completed.")

    def update_action_memory(self, llm_str):
        """Write agent actions to JSON file"""
        mem_file_path = os.path.join(self.memory_path, 'mem.json')
        lock_file_path = mem_file_path + ".lock"  # Create a lock file
        with FileLock(lock_file_path):
            # Load existing mem.json file or create a new one if not found
            if os.path.exists(mem_file_path):
                with open(mem_file_path, 'r') as f:
                    mem_data = json.load(f)
            else:
                mem_data = {}
            # Ensure that self.username has a list in mem_data
            if self.username not in mem_data:
                mem_data[self.username] = []
            # Append the current ai_message to the list
            mem_data[self.username].append(llm_str)
            # Write the updated data back to mem.json
            with open(mem_file_path, 'w') as f:
                json.dump(mem_data, f, indent=4)

    def write_to_chat_log(self, message):
        """Write the chat message to the chat log file"""
        chat_log_path = os.path.join(self.memory_path, 'chat_log.json')
        lock_file_path = chat_log_path + ".lock"  # Path for the lock file

        chat_entry = f"{self.username}: {message}"  # Format the message as "username: message"

        try:
            # Use FileLock to manage file locking
            with FileLock(lock_file_path):
                # Read the current chat log
                if os.path.exists(chat_log_path):
                    with open(chat_log_path, 'r') as chat_file:
                        chat_log = json.load(chat_file)
                else:
                    chat_log = {}

                # Add the new message to the list
                if "obs_entries" not in chat_log:
                    chat_log["obs_entries"] = []
                chat_log["obs_entries"].append(chat_entry)

                # Write the updated chat log back to the file
                with open(chat_log_path, 'w') as chat_file:
                    json.dump(chat_log, chat_file, indent=2)

        except Exception as e:
            self.logger.failed(f"Error reading or writing chat log file: {e}")
    
    def update_observation(self, goal_str=None, cur_action=None):
        """Based on current observation, send a chat message to the team"""
        # Chat a msg to team
        system_message = self.render_system_message(goal_str=goal_str)
        human_message = self.render_human_message(cur_action=cur_action)
        self.messages = [system_message, human_message]
        ai_message = call_with_messages(self.messages, model_type=self.model_type, dashscope_model=self.dashscope_model)
        self.logger.info("LLM response content in chatMessage: " + ai_message.content)
        # Parse AI response
        try:
            response = json.loads(ai_message.content)
            message_str = response.get("chat")
            self.write_to_chat_log(message_str)
            # self.run_skill_func(func_call_str=f"chatMessage(bot, \"{message_str}\")")
        except json.JSONDecodeError:
            self.logger.failed("Failed to decode AI response:", ai_message.content)

    def render_latest_chat_log(self, count=10):
        """
        Render the latest 'obs' entry for each player and 'count' most recent non-'obs' messages from the chat_log.json file.
        
        Args:
            team_name (str): The name of the team whose chat log to parse.
            count (int): The number of latest non-'obs' messages to retrieve.

        Returns:
            str: A JSON string containing the latest 'obs' entry for each player and 'count' most recent non-'obs' messages.
                If the chat log is empty, returns "empty".
                If an error occurs, returns an error message in JSON format.
        """
        # Define the path to the chat_log.json file
        chat_log_path = f'memory/{self.team_name}/chat_log.json'
        
        # Check if the file exists
        if not os.path.exists(chat_log_path):
            return json.dumps({"error": "chat_log.json file not found."})
        
        try:
            # Read and parse the chat log file
            with open(chat_log_path, 'r', encoding='utf-8', errors='ignore') as file:
                chat_log = json.load(file)
            
            # Check if chat_log is empty
            if not chat_log.get('obs_entries') and not any(chat_log.values()):
                return "empty"
            
            # Initialize dictionaries to store the latest 'obs' entry for each player
            latest_obs = {}
            all_non_obs_messages = []

            # Collect the latest 'obs' entry for each player
            # We assume that obs_entries are already sorted by time, so we can use them directly
            for entry in chat_log.get('obs_entries', []):
                player_name = entry.split(':')[0]
                if player_name not in latest_obs:
                    latest_obs[player_name] = entry
            
            # Collect all non-'obs' messages in chronological order
            for key in chat_log:  # Directly iterate over keys (already in chronological order)
                if key != 'obs_entries':
                    all_non_obs_messages.extend(chat_log[key])  # Add messages in original order
            
            # Get the last 'count' non-'obs' messages
            latest_non_obs = all_non_obs_messages[-count:] if len(all_non_obs_messages) > count else all_non_obs_messages
            
            # Combine the results
            combined_results = {"latest_observation": latest_obs, "latest_chat": latest_non_obs}
            
            # Convert the result to JSON string
            return json.dumps(combined_results, indent=2)
        
        except Exception as e:
            return json.dumps({"error": str(e)})
        
    def read_chat(self):
        """Read and summary the chat log (latest 50 entries)"""
        # Load the prompt template
        prompt_template = load_prompt("chat_summary")
        # Replace the placeholder with the actual username
        system_message_content = prompt_template.format(username=self.username)
        system_message = SystemMessage(content=system_message_content)
        human_message = HumanMessage(content=self.render_latest_chat_log(count=50))
        self.messages = [system_message, human_message]
        ai_message = call_with_messages(self.messages, model_type=self.model_type, dashscope_model=self.dashscope_model)
        self.logger.info("LLM response content in chat log reading: " + ai_message.content)
        return ai_message.content
    
    def extract_json_from_markdown(self, content):
        json_pattern = r"```json\n(.*?)\n```"
        match = re.search(json_pattern, content, re.DOTALL)
        if match:
            json_str = match.group(1)
            try:
                return json.loads(json_str)
            except json.JSONDecodeError as e:
                self.logger.error("Failed to parse JSON:", {e})
        return None
    
    def process_mc_img(self, url):
        messages = [SystemMessage(content=''), HumanMessage(content=load_prompt("img"))]
        ai_message = call_with_messages(messages, self.model_type, mode='vision', input_url=url)
        return ai_message.content