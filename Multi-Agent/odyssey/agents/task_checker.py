import os
import json
import datetime
from collections import defaultdict
from odyssey.utils.logger import get_logger, Timer

class TaskChecker:
    def __init__(
            self,
            memory_dir=None,
            memory_path=None,
            team_name=None,
            username=None,
            task_scenario=None
        ):

        self.team_name = team_name
        self.username = username
        self.memory_dir = memory_dir
        self.memory_path = memory_path
        self.task_scenario = task_scenario
        self.logger = get_logger("MC-Multi-Agent")
        self.results_path = os.path.join(os.getcwd(), 'results')
        os.makedirs(self.results_path, exist_ok=True)

    def combat_scene_initial(self, test_scene):
        """Initialize the combat scene based on the given test scene."""
        scene_map = {
            'End': 'Your team\'s ultimate goal is to beat the ender_dragon in the end. In order to defeat the Ender Dragon, the end_crystal needs to be destroyed first (also use combatWithEntity), otherwise the Ender Dragon will keep recovering. A total of ten Ender crystals are located on ten tall obsidian pillars, attempting to destroy them with ranged attacks. There will be many Endermen nearby, but defeating them is not the main task, combat with them only if necessary.',
            'Nether': 'Your team\'s ultimate goal is to beat the wither in the nether. Meele combat will be more effective because when the wither\'s health drops below 150, ranged attacks will not be able to damage it. There may be other nether monsters spawn around, combat with them if necessary.',
            'Ocean': 'Your team\'s ultimate goal is to beat the elder guardian in the ocean monument. Four guardians will spawn around, you also need to combat with them if necessary. The elder guardian may dive into the water. Both ranged and meele combat should be considered.',
        }
        scene_str = scene_map.get(test_scene, 'an unknown enemy')
        return scene_str

    def get_team_inventory(self):
        obs_file_path = os.path.join(self.memory_path, 'obs')
        # Initialize a defaultdict to store the total inventory
        team_inventory = defaultdict(int)
        # Iterate over all files in the directory
        for filename in os.listdir(obs_file_path):
            if filename.endswith('.json'):  # Only process JSON files
                file_path = os.path.join(obs_file_path, filename)
                # Read and parse the JSON file
                with open(file_path, 'r') as file:
                    try:
                        data = json.load(file)
                        # Extract the inventory dictionary
                        inventory = data.get('inventory', {})
                        # Add each item's quantity to the team inventory
                        for item, quantity in inventory.items():
                            team_inventory[item] += quantity
                    except json.JSONDecodeError:
                        self.logger.failed(f"Error decoding JSON file: {filename}")
                    except Exception as e:
                        self.logger.failed(f"Error reading file {filename}: {e}")
        # Convert defaultdict to a regular dictionary before returning
        return dict(team_inventory)

    def check_resource_task(self, item_dict):
        """Check whether the resource task is complete"""
        # Get the team's inventory
        team_inventory = self.get_team_inventory()
        # Initialize variables
        all_items_met = True  # To track if all items have met the required quantity
        progress_info = ""    # To store progress information as a string
        # Check if team_inventory has all items in item_dict with at least the required quantity
        for item, required_quantity in item_dict.items():
            # Get the current quantity from the team inventory, default to 0 if item is not found
            current_quantity = team_inventory.get(item, 0)
            # Append progress information to the progress_info string
            if current_quantity < required_quantity:
                progress_info += f"{item}: {current_quantity}/{required_quantity}  "  # Add progress info
                all_items_met = False  # Mark that not all items are met
            else:
                progress_info += f"{item}: {current_quantity}/{required_quantity} (Complete)  "  # Add completion info
        # Return whether all items met their required quantity and the progress information
        return all_items_met, progress_info

    def check_combat_task(self):
        """Check whether the combat task is complete"""
        chat_log_path = os.path.join(self.memory_path, 'chat_log.json')
        try:
            # Read the chat_log.json file
            with open(chat_log_path, 'r', encoding='utf-8', errors='ignore') as file:
                chat_log = json.load(file)
            # Iterate through all logs in chat_log
            for day_log in chat_log.values():  # day_log is a list of messages for a specific timestamp
                for message in day_log:  # Check each message in the day's log
                    if "SystemInfo: Success" in message:
                        return True  # Combat task is complete
            if self.check_agent_death():
                return True  # Combat task is complete if agent is dead
            return False
        except FileNotFoundError:
            self.logger.failed(f"Error: {chat_log_path} not found.")
            return False
        except json.JSONDecodeError:
            self.logger.failed(f"Error: {chat_log_path} is not a valid JSON file.")
            return False
        except Exception as e:
            self.logger.failed(f"Error: {e}")
            return False
        
    def check_agent_death(self):
        # Construct the path to the obs.json file
        obs_file_path = os.path.join(self.memory_path, 'obs', f"{self.username}.json")
        
        try:
            # Check if the file exists
            if not os.path.exists(obs_file_path):
                self.logger.error(f"Observation file not found: {obs_file_path}")
                return False
            
            # Read the file content
            with open(obs_file_path, 'r') as f:
                obs_data = json.load(f)
            
            # Check if health is 0
            if obs_data.get("health") == 0:
                self.logger.debug(f"Agent {self.username} has died (health is 0).")
                return True
            else:
                self.logger.debug(f"Agent {self.username} is alive (health is {obs_data.get('health')}).")
                return False
        
        except Exception as e:
            self.logger.error(f"Error reading observation file: {e}")
            return False 

    def check_pvp_task(self):
        """Check whether the PVP task is complete."""
        # Get all team directories
        teams = [d for d in os.listdir(self.memory_dir) if os.path.isdir(os.path.join(self.memory_dir, d))]
        if len(teams) != 2:
            self.logger.critical("Error: There must be exactly two teams.")
            return False

        team_a, team_b = teams[0], teams[1]
        team_a_defeated = self._is_team_defeated(team_a)
        team_b_defeated = self._is_team_defeated(team_b)

        if team_a_defeated:
            self.logger.success(f"{team_b} beat {team_a}!")
            return True
        elif team_b_defeated:
            self.logger.success(f"{team_a} beat {team_b}!")
            return True

        return False

    def _is_team_defeated(self, team_name):
        """Check if all players in a team have health 0."""
        team_dir = os.path.join(self.memory_dir, team_name, "obs")
        if not os.path.exists(team_dir):
            print(f"Error: Team directory {team_dir} does not exist.")
            return False

        # Iterate through all player observation files in the team directory
        for filename in os.listdir(team_dir):
            if filename.endswith(".json"):
                file_path = os.path.join(team_dir, filename)
                with open(file_path, "r", encoding="utf-8") as f:
                    try:
                        data = json.load(f)
                        if data.get("health", 1) > 0:  # If any player has health > 0, team is not defeated
                            return False
                    except json.JSONDecodeError:
                        print(f"Error: Failed to parse {file_path}.")
                        continue
        return True  # All players have health 0

    def evaluate_task(self, item_dict=None, combat_scene=None):
        """Check whether the task is complete"""
        progress_info = None
        if self.task_scenario == 'resource':
            completed, progress_info = self.check_resource_task(item_dict)
        elif self.task_scenario == 'combat':
            completed = self.check_combat_task()
        elif self.task_scenario == 'pvp':
            completed = self.check_pvp_task()
        else:
            completed = False
        return completed, progress_info

    def log_results(self, combat_scene, item_dict, total_time=None, skill_total_time=None):
        """
        Logs the total execution time for the current player and each function call type to a JSON file.
        If self.task_scenario is 'combat' or 'pvp', also logs the player's health from the observation file
        and the lowest boss health for 'combat' task from the chat log.

        Args:
            combat_scene (str): The combat scene name.
            item_dict (dict): The dictionary of items used by the player.
            total_time (float, optional): The total execution time. Defaults to None.
            skill_total_time (float, optional): The total skill execution time. Defaults to None.
            llm_total_time (float, optional): The total LLM execution time. Defaults to None.
        """
        # Define the paths
        obs_file_path = os.path.join(self.memory_path, 'obs', f'{self.username}.json')
        chat_log_path = os.path.join(self.memory_path, 'chat_log.json')
        results_dir = os.path.join(self.results_path, self.task_scenario)  # Save to result/{self.task_scenario}

        # Ensure the results directory exists
        if not os.path.exists(results_dir):
            os.makedirs(results_dir)

        # Initialize the result dictionary
        result = {
            "username": self.username,
            "team_name": self.team_name,
            "task_scenario": self.task_scenario,
            "combat_scene": combat_scene,
            "item_dict": item_dict,
            "total_time": total_time if total_time is not None else 0.0,
            "skill_total_time": skill_total_time if skill_total_time is not None else 0.0,
            "health": None,  # Only populated if self.task_scenario is 'combat' or 'pvp'
            "lowest_boss_health": None,  # Only populated if self.task_scenario is 'combat' or 'pvp'
            "timestamp": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        # If self.task_scenario is 'combat' or 'pvp', read health from the observation file
        if self.task_scenario == 'combat' or self.task_scenario == 'pvp':
            if os.path.exists(obs_file_path):
                with open(obs_file_path, 'r') as file:
                    obs_data = json.load(file)
                    result["health"] = obs_data.get("health", None)
            else:
                self.logger.failed(f"Observation file not found for {self.username}. Health data will not be recorded.")

            # Read the chat log to find the lowest boss health
            if os.path.exists(chat_log_path):
                with open(chat_log_path, 'r', encoding='utf-8', errors='ignore') as file:
                    chat_log_data = json.load(file)
                    lowest_boss_health = self._extract_lowest_boss_health(chat_log_data)
                    result["lowest_boss_health"] = lowest_boss_health
            else:
                self.logger.failed(f"Chat log file not found for {self.username}. Lowest boss health data will not be recorded.")

        # Define the result file name
        if self.task_scenario == 'combat':
            result_file_name = f"{combat_scene}.json"
        elif self.task_scenario == 'resource':
            result_file_name = f"resource_player_data.json"
        elif self.task_scenario == 'pvp':
            result_file_name = f"pvp_player_data.json"
        result_file_path = os.path.join(results_dir, result_file_name)

        # Load existing results if the file exists
        try:
            if os.path.exists(result_file_path):
                with open(result_file_path, 'r') as file:
                    existing_results = json.load(file)
                    # Ensure existing_results is a list
                    if not isinstance(existing_results, list):
                        raise ValueError(f"File {result_file_path} does not contain a valid list of results.")
            else:
                existing_results = []
        except (json.JSONDecodeError, ValueError) as e:
            self.logger.failed(f"Failed to load existing results from {result_file_path}: {e}")
            existing_results = []

        # Append the new result to the existing results
        existing_results.append(result)

        # Save the updated results to the file
        try:
            with open(result_file_path, 'w') as file:
                json.dump(existing_results, file, indent=4)
            self.logger.success(f"Results have been logged to {result_file_path}")
        except Exception as e:
            self.logger.failed(f"Failed to save results to {result_file_path}: {e}")

    def _extract_lowest_boss_health(self, chat_log_data):
        """
        Extracts the lowest boss health from the chat log data.

        Args:
            chat_log_data (dict): The chat log data loaded from chat_log.json.

        Returns:
            int or None: The lowest boss health found in the chat log, or None if no health data is found.
        """
        lowest_boss_health = None

        # Iterate through all chat entries
        for entries in chat_log_data.values():
            for entry in entries:
                if isinstance(entry, str) and "Boss Health:" in entry:
                    # Extract the boss health value from the chat entry
                    try:
                        health_value = int(entry.split("Boss Health:")[1].strip())
                        if lowest_boss_health is None or health_value < lowest_boss_health:
                            lowest_boss_health = health_value
                    except (IndexError, ValueError):
                        # Skip if the health value cannot be extracted
                        continue

        return lowest_boss_health