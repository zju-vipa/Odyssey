import copy
import json
import os
import re
import time
import threading
import queue
import base64
from typing import Dict
from .env import VoyagerEnv

from .agents import SkillManager
from .agents import MemoryManager
from .agents import TaskChecker

from .agents.llm import call_with_messages, ModelType
from .utils.logger import get_logger, Timer

class Odyssey:
    def __init__(
        self,
        mc_host: str = 'localhost',
        mc_port: int = 25565,
        azure_login: Dict[str, str] = None,
        server_port: int = 3000,
        viewer_port: int = 3100,
        environment: str = None,
        env_wait_ticks: int = 20,
        env_request_timeout: int = 600,
        model_type: str = ModelType.ALI,
        dashscope_model: str = 'qwen-plus',
        vision_dashscope_model: str = 'qwen-vl-plus',
        model_id: int = 1, # one LLM for one agent
        chat_log_cnt = 10,
        username = 'bot',
        memory_dir = 'memory',
        task_scenario = None,
        team_name = None,
        team_prompt = None
    ):
        # init env
        self.username = username
        self.logger = get_logger("MC-Multi-Agent")
        self.env = VoyagerEnv(
            mc_host=mc_host,
            mc_port=mc_port,
            azure_login=azure_login,
            server_port=server_port,
            viewer_port=viewer_port,
            request_timeout=env_request_timeout,
            task_scenario=task_scenario
        )
        self.env_wait_ticks = env_wait_ticks
        self.chat_log_cnt = chat_log_cnt
        self.totoal_time = 0 
        self.total_iter = 0 
        self.step_time = []
        self.model_type = model_type
        self.dashscope_model = dashscope_model
        self.vision_dashscope_model = vision_dashscope_model
        self.model_id = model_id
        self.chat_queue = queue.Queue()
        self.task_queue = queue.Queue(maxsize=1)
        self.cur_action = None # the skill currently executing
        self.interrupt_flag = False
        self.is_running = True
        self.memory_dir = memory_dir
        self.task_scenario = task_scenario
        self.team_name = team_name
        self.team_prompt = team_prompt
        self.task_completed = False
        if memory_dir and team_name:
            self.team_memory_dir = f"{memory_dir}/{team_name}"
        else:
            self.team_memory_dir = memory_dir or 'memory'
        self.memory_path = os.path.join(os.getcwd(), self.team_memory_dir)
        os.makedirs(self.memory_path, exist_ok=True)

        # init agents
        self.skill_manager = SkillManager()
        self.task_checker = TaskChecker(team_name=self.team_name, username=self.username, memory_dir=memory_dir, memory_path=self.memory_path, task_scenario=task_scenario)
        self.memory_manager = MemoryManager(team_name=self.team_name, username=self.username, memory_dir=memory_dir, memory_path=self.memory_path, model_type=model_type, dashscope_model=dashscope_model)

        self.environment = environment
        self.skills = [[], []]

        self.context = ""
        self.messages = None
        self.conversations = []
        self.last_events = None

    def env_reset(self, mode="soft"):
        self.env.reset(
                options={
                    "mode": mode,
                    "wait_ticks": self.env_wait_ticks,
                    "username": self.username,
                    "team_name": self.team_name
                }
            )

    def run_skill_func(self, func_call_str, log_time=False):
        start_time = time.time()
        retry = 3
        # Preprocess the function call string
        func_call_str = self.skill_manager.preprocess_func_call_str(func_call_str)

        while retry > 0:
            try:
                # Directly use the processed func_call_str for execution
                exec_code = f"await {func_call_str}"
                break
            except Exception as e:
                retry -= 1
                exec_code = f"Error creating exec_code: {e}"

        result = ''
        if "Error" not in exec_code:
            # Execute the constructed JavaScript code
            events = self.env.step(
                exec_code,
                programs=self.skill_manager.programs,
            )
        else:
            self.logger.warning(f"{exec_code} Code execution error!")
            events = None
        end_time = time.time()
        execution_time = end_time - start_time
        # If logging is enabled, record the execution time and function call string
        if log_time:
            log_time_path = os.path.join(os.getcwd(), 'results/skill_time.json')
            # Ensure the directory exists
            os.makedirs(os.path.dirname(log_time_path), exist_ok=True)
            new_entry = {'func_call_str': func_call_str, 'execution_time': execution_time}
            # Read existing entries if any
            if os.path.exists(log_time_path):
                with open(log_time_path, 'r') as file:
                    time_logs = json.load(file)
            else:
                time_logs = []
            # Append the new entry
            time_logs.append(new_entry)
            # Write back to the file
            with open(log_time_path, 'w') as file:
                json.dump(time_logs, file, indent=4)
                self.logger.success(f'Logged skill execution time to {log_time_path}')
        return events

    def initialize_task(self, item_dict=None, combat_scene=None):
        """Initialize the task based on the given task scene."""
        if self.task_scenario == 'resource':
            goal_str = f'Your ultimate goal is to obtain {item_dict}. Communicate with your team, divide your work properly, and make sure that every step is moving toward that goal!'
        elif self.task_scenario == 'combat':
            self.run_skill_func(f'initialInventory(bot, {item_dict})')
            self.run_skill_func(f'teleportToCombatScene(bot, \'{combat_scene}\')')
            scene_str = self.task_checker.combat_scene_initial(combat_scene)
            goal_str = (f"{scene_str} Instead of collecting resources, you are given battle supplies directly, "
                        "communicate with your teammates, develop a workable collaborative combat plan, and defeat the enemy! ")
        elif self.task_scenario == 'explore':
            goal_str = 'There is no specific goal, keep communicating with your team, collect various resources, make novel discoveries and explore the world!'
        elif self.task_scenario == 'pvp':
            goal_str = 'You are in a PVP task. Your goal is to defeat the enemy team. Collaborate with your team, develop a workable collaborative combat plan, and defeat the enemy!'
            self.run_skill_func(f'initialInventory(bot, {item_dict})')
            self.run_skill_func(f'teleportToPvpScene(bot)')
        else:
            goal_str = ''

        return goal_str

    def start_agent_serially(self, item_dict=None, combat_scene=None):
        """Only used for ablation study"""
        self.memory_manager.memory_reset()
        goal_str = self.initialize_task(item_dict, combat_scene)
        start_time = time.time()

        while not self.task_completed:
            try:
                self.memory_manager.update_observation(goal_str=goal_str, cur_action=self.cur_action)
                completed, progress_info = self.task_checker.evaluate_task(item_dict, combat_scene)
                self.task_completed = completed
                if self.task_completed:
                    self.logger.debug(f"LLM task exiting: task_completed={self.task_completed}")
                    break  # Exit the loop if task is completed

                system_message = self.skill_manager.render_system_message(self.task_scenario)
                information = self.render_information(progress_info=progress_info)
                human_message = self.skill_manager.render_human_message(goal_str, self.cur_action, information)
                self.messages = [system_message, human_message]
                self.logger.info("obs in step:" + human_message.content)
                ai_message = call_with_messages(self.messages, self.model_type, self.model_id)
                self.logger.success("LLM response content in step:" + ai_message.content)
                self.memory_manager.update_action_memory(llm_str=ai_message.content)
                # Parse JSON response
                try:
                    # Try to parse ai_message.content directly as JSON
                    response = json.loads(ai_message.content)
                except json.JSONDecodeError:
                    # If direct parsing fails, fall back to extracting JSON from Markdown
                    response = self.memory_manager.extract_json_from_markdown(ai_message.content)
                func_call_str = response.get("skill")
                if func_call_str:
                    # Replace "True" or "False" (case-insensitive) with lowercase versions for JavaScript execution
                    func_call_str = re.sub(r'\bTrue\b', 'true', func_call_str, flags=re.IGNORECASE)
                    func_call_str = re.sub(r'\bFalse\b', 'false', func_call_str, flags=re.IGNORECASE)
                    self.run_skill_func(func_call_str=func_call_str)
            except Exception as e:
                continue
        
        # Log total program execution time
        end_time = time.time()
        execution_time = end_time - start_time
        # Log results
        self.task_checker.log_results(combat_scene=combat_scene, item_dict=item_dict, total_time=execution_time)
        self.logger.success(f"Results logged for {self.username} in {self.team_name}")
        self.env.close()
        return
                    
    def start_agent(self, item_dict=None, combat_scene=None, mode='text'):
        """Start the agent to continuously process tasks from LLM responses and execute skills."""
        self.memory_manager.memory_reset()
        # Initialize the task and get the goal string
        goal_str = self.initialize_task(item_dict, combat_scene)
        # Create an event to signal thread exit
        self.exit_event = threading.Event()
        start_time = time.time()

        # Variables to track thread execution time
        skill_thread_start_time = None
        skill_thread_total_time = 0

        # Define the LLM task in a thread
        def llm_task():
            nonlocal skill_thread_start_time, skill_thread_total_time
            while not self.exit_event.is_set():
                try:
                    # Update observation after skill execution starts
                    self.memory_manager.update_observation(goal_str=goal_str, cur_action=self.cur_action)

                    # Check task success right after observation updates
                    if self.task_scenario != 'explore':  # Explore can be endless
                        completed, progress_info = self.task_checker.evaluate_task(item_dict, combat_scene)
                        self.task_completed = completed

                    # Exit if task is completed (or agent is dead in combat task)
                    if self.task_completed:
                        self.logger.debug(f"LLM task exiting: task_completed={self.task_completed}")
                        self.exit_event.set()  # Signal all threads to exit
                        break  # Exit the thread

                    # Plan next skill
                    system_message = self.skill_manager.render_system_message(self.task_scenario)
                    information = self.render_information(progress_info=progress_info, mode=mode)
                    human_message = self.skill_manager.render_human_message(goal_str, self.cur_action, information)
                    self.messages = [system_message, human_message]
                    self.logger.info("obs in step:" + human_message.content)

                    # Retry LLM call indefinitely until successful
                    while not self.exit_event.is_set():
                        try:
                            ai_message = call_with_messages(self.messages, self.model_type, self.model_id)
                            self.logger.success("LLM response content in step:" + ai_message.content)
                            self.memory_manager.update_action_memory(llm_str=ai_message.content)

                            # Parse JSON response
                            try:
                                # Try to parse ai_message.content directly as JSON
                                response = json.loads(ai_message.content)
                            except json.JSONDecodeError:
                                # If direct parsing fails, fall back to extracting JSON from Markdown
                                response = self.memory_manager.extract_json_from_markdown(ai_message.content)
                            func_call_str = response.get("skill")
                            if func_call_str:
                                # Replace "True" or "False" (case-insensitive) with lowercase versions for JavaScript execution
                                func_call_str = re.sub(r'\bTrue\b', 'true', func_call_str, flags=re.IGNORECASE)
                                func_call_str = re.sub(r'\bFalse\b', 'false', func_call_str, flags=re.IGNORECASE)
                            self.interrupt_flag = response.get("interrupt")
                            if self.interrupt_flag:
                                self.env.close()
                                self.env_reset()
                                self.interrupt_flag = False  # Reset interrupt flag
                                start_skill_thread()  # Restart skill thread after env_reset

                            # Store the func_call_str in the task queue
                            if self.task_queue.full():
                                # Remove the first task if the queue is full
                                self.task_queue.get_nowait()
                            self.task_queue.put(func_call_str)  # Store the func_call_str in the queue
                            break  # Exit the retry loop if successful
                        except json.JSONDecodeError as e:
                            self.logger.failed("Failed to decode AI response:", ai_message.content, "error: ", e)
                            # Retry the LLM call
                            continue
                        except Exception as e:
                            self.logger.error(f"Exception in LLM call: {e}")
                            break # Exit the thread if LLM call fails for non-JSONDecodeError reasons
                except Exception as e:
                    self.logger.error(f"Exception in llm_task: {e}")
                    # Continue the loop to retry
                    continue

        # Start the LLM task in a separate thread
        llm_thread = threading.Thread(target=llm_task, daemon=True)
        llm_thread.start()

        # Function to start a skill execution thread
        def start_skill_thread():
            nonlocal skill_thread_start_time, skill_thread_total_time
            if skill_thread_start_time is not None:
                # If skill thread was previously running, record its execution time
                skill_thread_total_time += time.time() - skill_thread_start_time
            skill_thread_start_time = time.time()  # Record start time for the new thread

            # Process the current skill from the task queue in a separate thread
            def skill_execution():
                nonlocal skill_thread_start_time, skill_thread_total_time
                try:
                    while not self.exit_event.is_set():
                        try:
                            func_call_str = self.task_queue.get(timeout=0.1)  # Wait for 0.1 seconds, prevent blocking
                            self.cur_action = func_call_str
                            self.run_skill_func(func_call_str=func_call_str)
                            self.task_completed = self.task_checker.evaluate_task(item_dict, combat_scene)[0] # Check task success after each skill execution
                            # Exit if task is completed or agent is dead
                            if self.task_completed:
                                self.logger.info(f"Skill execution exiting: task_completed={self.task_completed}")
                                self.exit_event.set()  # Signal all threads to exit
                                break  # Exit the thread

                            self.interrupt_flag = False
                        except queue.Empty:
                            # If the queue is empty, continue the loop
                            continue
                        except Exception as e:
                            self.logger.error(f"Exception in skill_execution: {e}")
                            break  # Exit the skill thread for non-queue.Empty exceptions in combat task
                finally:
                    # Ensure total time is updated even if the thread exits unexpectedly
                    if skill_thread_start_time is not None:
                        skill_thread_total_time += time.time() - skill_thread_start_time
                        skill_thread_start_time = None  # Reset start time after thread exits

            skill_thread = threading.Thread(target=skill_execution, daemon=True)
            skill_thread.start()

        # Initial call to start skill execution
        start_skill_thread()

        # Wait for the LLM thread to complete
        llm_thread.join()

        # Ensure skill thread is also terminated
        self.logger.debug(f"Main thread exiting: task_completed={self.task_completed}")

        # Log total program execution time
        end_time = time.time()
        execution_time = end_time - start_time
        # Log results
        self.task_checker.log_results(combat_scene=combat_scene, item_dict=item_dict, total_time=execution_time, skill_total_time=skill_thread_total_time)
        self.logger.success(f"Results logged for {self.username} in {self.team_name}")
        self.env.close()
        return
 
    def render_information(self, progress_info=None, mode='text'):
        """Render step information as input for LLM"""
        self_obs = self.memory_manager.render_user_observation()
        chat_log = self.memory_manager.render_latest_chat_log(count = self.chat_log_cnt)
        progress_info_str = f"Resource Collection Progress: {progress_info}" if progress_info else ''
        
        if mode == 'vision':
            url = None
            self_obs = ''
            image_path = os.path.join(self.memory_path, f'screen/{self.username}.png')
            if os.path.exists(image_path):
                with open(image_path, 'rb') as image_file:
                    image_data = image_file.read()
                    base64_encoded = base64.b64encode(image_data).decode('utf-8')
                    url = f'data:image/png;base64,{base64_encoded}'
                    self_obs = self.memory_manager.process_mc_img(url)

        information = (
            f"You are {self.username}. {' ' + self.team_prompt if self.team_prompt else ''}\n"
            f"{progress_info_str}\n"
            f"Your status information: {self_obs}\n"
            f"Latest chat messages: {chat_log}\n"
        )
        return information

    def human_player_listener(self, human_player_name, team_name):
        # Launch a mineflayer bot specifically designed to monitor human player status and chat messages
        self.env_reset()
        self.run_skill_func(func_call_str=f"listenHumanPlayer(bot, '{human_player_name}', '{team_name}')")
        if self.task_completed:
            self.env.close()
        return
    
    def system_controller(self, team_name, item_dict, combat_scene, username_list):
        self.env_reset(mode="hard")
        if self.task_scenario == 'combat':
            self.run_skill_func(func_call_str=f"initializeCombatScene(bot, '{team_name}', '{combat_scene}', {username_list})")
        elif self.task_scenario == 'resource':
            item_dict_str = ", ".join(f"{key}:{value}" for key, value in item_dict.items())
            self.run_skill_func(func_call_str=f"initializeResourceScene(bot, '{team_name}', '{item_dict_str}', {username_list})")
        elif self.task_scenario == 'pvp':
            self.run_skill_func(func_call_str=f"initializePVPScene(bot, {username_list})")
        else:
            return # placeholder for future task scenarios
        if self.task_completed:
            self.env.close()
        return
    
    def close(self):
        # for external call
        self.env.close()