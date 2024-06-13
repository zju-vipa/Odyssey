import copy
import json
import os
import time
from typing import Dict

from javascript import require
import odyssey.utils as U
from .env import VoyagerEnv

from .agents import ActionAgent
from .agents import CommentAgent
from .agents import CriticAgent
from .agents import PlanerAgent
from .agents import SkillManager

# add llama
from .agents.llama import call_with_messages, ModelType
from .utils.logger import get_logger, Timer

# TODO: remove event memory
class Odyssey:
    def __init__(
        self,
        mc_host: str = 'localhost',
        mc_port: int = None,
        azure_login: Dict[str, str] = None,
        server_port: int = 3000,
        environment: str = None,
        env_wait_ticks: int = 20,
        env_request_timeout: int = 600,
        max_iterations: int = 160,
        reset_placed_if_failed: bool = False,
        action_agent_model_name: str = ModelType.LLAMA3_8B_V3,
        action_agent_temperature: float = 0,
        action_agent_task_max_retries: int = 4,
        action_agent_show_chat_log: bool = True,
        action_agent_show_execution_error: bool = True,
        planer_agent_model_name: str = ModelType.LLAMA3_70B_V1,
        planer_agent_qa_model_name: str = ModelType.LLAMA3_8B_V3,
        planer_agent_warm_up: Dict[str, int] = None,
        planer_agent_core_inventory_items: str = r".*_log|.*_planks|stick|crafting_table|furnace"
        r"|cobblestone|dirt|coal|.*_pickaxe|.*_sword|.*_axe",
        planer_agent_mode: str = "auto",
        critic_agent_model_name: str = ModelType.LLAMA2_70B,
        comment_agent_model_name: str = ModelType.LLAMA3_8B_V3,
        critic_agent_temperature: float = 0,
        critic_agent_mode: str = "auto",
        skill_manager_temperature: float = 0,
        skill_manager_retrieval_top_k: int = 10,
        openai_api_request_timeout: int = 240,
        ckpt_dir: str = "ckpt",
        skill_library_dir: str = None,
        resume: bool = False,
        reload = False,
        embedding_dir = "",
        username = 'bot'
    ):
        """
        The main class for Odyssey.
        Action agent is the iterative prompting mechanism in paper.
        planer agent is the automatic planer in paper.
        Critic agent is the self-verification in paper.
        Skill manager is the skill library in paper.
        :param mc_port: minecraft in-game port
        :param azure_login: minecraft login config
        :param server_port: mineflayer port
        :param openai_api_key: openai api key
        :param env_wait_ticks: how many ticks at the end each step will wait, if you found some chat log missing,
        you should increase this value
        :param env_request_timeout: how many seconds to wait for each step, if the code execution exceeds this time,
        python side will terminate the connection and need to be resumed
        :param reset_placed_if_failed: whether to reset placed blocks if failed, useful for building task
        :param action_agent_model_name: action agent model name
        :param action_agent_temperature: action agent temperature
        :param action_agent_task_max_retries: how many times to retry if failed
        :param planer_agent_model_name: planer agent model name
        :param planer_agent_temperature: planer agent temperature
        :param planer_agent_qa_model_name: planer agent qa model name
        :param planer_agent_qa_temperature: planer agent qa temperature
        :param planer_agent_warm_up: info will show in planer human message
        if completed task larger than the value in dict, available keys are:
        {
            "context": int,
            "biome": int,
            "time": int,
            "other_blocks": int,
            "nearby_entities": int,
            "health": int,
            "hunger": int,
            "position": int,
            "equipment": int,
            "chests": int,
            "optional_inventory_items": int,
        }
        :param planer_agent_core_inventory_items: only show these items in inventory before optional_inventory_items
        reached in warm up
        :param planer_agent_mode: "auto" for automatic planer, "manual" for human planer
        :param critic_agent_model_name: critic agent model name
        :param critic_agent_temperature: critic agent temperature
        :param critic_agent_mode: "auto" for automatic critic ,"manual" for human critic
        :param skill_manager_model_name: skill manager model name
        :param skill_manager_temperature: skill manager temperature
        :param skill_manager_retrieval_top_k: how many skills to retrieve for each task
        :param openai_api_request_timeout: how many seconds to wait for openai api
        :param ckpt_dir: checkpoint dir
        :param skill_library_dir: skill library dir
        :param resume: whether to resume from checkpoint
        """
        # init env
        self.username = username
        self.logger = get_logger("Voyager")
        self.env = VoyagerEnv(
            mc_host=mc_host,
            mc_port=mc_port,
            azure_login=azure_login,
            server_port=server_port,
            request_timeout=env_request_timeout,
        )
        self.env_wait_ticks = env_wait_ticks
        self.reset_placed_if_failed = reset_placed_if_failed
        self.max_iterations = max_iterations
        self.totoal_time = 0 
        self.total_iter = 0 
        self.step_time = []
        self.action_agent_model_name = action_agent_model_name
        self.planer_agent_model_name = planer_agent_model_name
        self.planer_agent_qa_model_name = planer_agent_qa_model_name
        self.critic_agent_model_name = critic_agent_model_name
        self.comment_agent_model_name = comment_agent_model_name

        # set openai api key
        # os.environ["OPENAI_API_KEY"] = openai_api_key

        # init agents
        self.action_agent = ActionAgent(
            temperature=action_agent_temperature,
            request_timout=openai_api_request_timeout,
            ckpt_dir=ckpt_dir,
            resume=resume,
            chat_log=action_agent_show_chat_log,
            execution_error=action_agent_show_execution_error,
        )
        self.action_agent_task_max_retries = action_agent_task_max_retries
        self.planer_agent = PlanerAgent(
            model_name=planer_agent_model_name,
            # temperature=planer_agent_temperature,
            qa_model_name=planer_agent_qa_model_name,
            # qa_temperature=planer_agent_qa_temperature,
            request_timout=openai_api_request_timeout,
            ckpt_dir=ckpt_dir,
            resume=resume,
            mode=planer_agent_mode,
            warm_up=planer_agent_warm_up,
            core_inventory_items=planer_agent_core_inventory_items,
            embedding_model=embedding_dir,
        )
        self.critic_agent = CriticAgent(
            model_name=critic_agent_model_name,
            temperature=critic_agent_temperature,
            request_timout=openai_api_request_timeout,
            mode=critic_agent_mode,
        )
        self.comment_agent = CommentAgent(
            environment=environment,
            model_name=comment_agent_model_name
        )
        self.skill_manager = SkillManager(
            temperature=skill_manager_temperature,
            retrieval_top_k=skill_manager_retrieval_top_k,
            request_timout=openai_api_request_timeout,
            ckpt_dir=skill_library_dir if skill_library_dir else ckpt_dir,
            resume=True if resume or skill_library_dir else False,
            reload=reload,
            embedding_model=embedding_dir,
        )
        self.environment = environment
        self.skills = [[], []]
        self.recorder = U.EventRecorder(ckpt_dir=ckpt_dir, resume=resume)
        self.resume = resume

        # init variables for rollout
        self.action_agent_rollout_num_iter = -1
        self.task = None
        self.context = ""
        self.messages = None
        self.conversations = []
        self.last_events = None
        self.skill_library_dir = skill_library_dir

    def reset(self, task, context="", reset_env=True):
        self.action_agent_rollout_num_iter = 0
        self.task = task
        self.context = context
        if reset_env:
            self.env.reset(
                options={
                    "mode": "soft",
                    "wait_ticks": self.env_wait_ticks,
                    "username": self.username
                }
            )
        difficulty = (
            "easy" if len(self.planer_agent.completed_tasks) > 15 else "peaceful"
        )
        # step to peek an observation
        events = self.env.step(
            "bot.chat(`/time set ${getNextTime()}`);\n"
            + f"bot.chat('/difficulty {difficulty}');\n"
        )
        with Timer('retrieve skills'):
            self.skills = self.skill_manager.retrieve_skills(query=self.context)
            self.logger.info(f"Render Action Agent system message with {len(self.skills[0])} skills")
        system_message = self.action_agent.render_system_message()
        human_message = self.action_agent.render_human_message(
            events=events, code="", task=self.task, context=context, critique="", skills=self.skills[1]
        )
        self.messages = [system_message, human_message]
        self.logger.debug(f'Select Skill Human Message: {human_message.content}')
        # self.logger.debug(f"****Action Agent human message****\n{human_message.content}")
        assert len(self.messages) == 2
        self.conversations = []
        return self.messages

    def close(self):
        self.env.close()

    def step(self):
        if self.action_agent_rollout_num_iter < 0:
            raise ValueError("Agent must be reset before stepping")
        # ai_message = self.action_agent.llm(self.messages)
        # modify
        with Timer('step: Select Skill'):
            self.logger.debug(f'human mesasges: {self.messages[1].content}')
            ai_message = call_with_messages(self.messages, self.action_agent_model_name)
            self.logger.debug(f"response: {ai_message.content}")
        self.conversations.append(
            (self.messages[0].content, self.messages[1].content, ai_message.content)
        )
        with Timer('Process Select Skill Response'):
            parsed_result = self.action_agent.process_ai_message(message=ai_message, skills=self.skills[0])
            self.logger.debug(f"parsed_result: {parsed_result}")

        success = False
        cur_inventoty = ""
        if isinstance(parsed_result, dict):
            code = parsed_result["program_code"] + "\n" + parsed_result["exec_code"]
            with Timer('env step'):
                events = self.env.step(
                    code,
                    programs=self.skill_manager.programs,
                )
            self.totoal_time, self.total_iter = self.recorder.record(events, self.task)
            self.action_agent.update_chest_memory(events[-1][1]["nearbyChests"])
            if self.environment == 'subgoal':
                with Timer('Check Subgoal Success'):
                    success = self.critic_agent.check_subgoal_success(
                        events=events,
                        task=self.task,
                    )
                    critique = ''
                    self.logger.debug(f'success: {success}')
            else:
                with Timer('Critic Check Task Success'):
                    success, critique = self.critic_agent.check_task_success(
                        events=events,
                        task=self.task,
                        context=self.context,
                        chest_observation=self.action_agent.render_chest_observation(),
                        max_retries=5,
                        
                    )
                    self.logger.debug(f'success: {success}')
                    self.logger.debug(f'critique: {critique}')

            if self.reset_placed_if_failed and not success:
                # revert all the placing event in the last step
                blocks = []
                positions = []
                for event_type, event in events:
                    if event_type == "onSave" and event["onSave"].endswith("_placed"):
                        block = event["onSave"].split("_placed")[0]
                        position = event["status"]["position"]
                        blocks.append(block)
                        positions.append(position)
                new_events = self.env.step(
                    f"await givePlacedItemBack(bot, {U.json_dumps(blocks)}, {U.json_dumps(positions)})",
                    programs=self.skill_manager.programs,
                )
                events[-1][1]["inventory"] = new_events[-1][1]["inventory"]
                events[-1][1]["voxels"] = new_events[-1][1]["voxels"]
            # new_skills = self.skill_manager.retrieve_skills(
            #     query=self.context
            #     + "\n\n"
            #     + self.action_agent.summarize_chatlog(events)
            # )
            system_message = self.action_agent.render_system_message()
            human_message = self.action_agent.render_human_message(
                events=events,
                code=parsed_result["program_name"],
                task=self.task,
                critique=critique,
                skills=self.skills[1]
            )
            self.last_events = copy.deepcopy(events)
            self.messages = [system_message, human_message]
        else:
            assert isinstance(parsed_result, str)
            self.totoal_time, self.total_iter = self.recorder.record([], self.task)
            self.logger.warning(f"{parsed_result} Trying again!")
        self.step_time.append(self.totoal_time)
        self.logger.info(self.totoal_time)
        assert len(self.messages) == 2
        self.action_agent_rollout_num_iter += 1
        done = (
            self.action_agent_rollout_num_iter >= self.action_agent_task_max_retries
            or success
        )
        info = {
            "task": self.task,
            "success": success,
            "conversations": self.conversations,
        }
        if success:
            assert (
                "program_code" in parsed_result and "program_name" in parsed_result
            ), "program and program_name must be returned when success"
            info["program_code"] = parsed_result["program_code"]
            info["program_name"] = parsed_result["program_name"]
        # else:
        #     self.logger.debug(f"****Action Agent human message****\n{self.messages[-1].content}")
        return self.messages, self.last_events[-1][1]["inventory"], done, info

    def rollout(self, *, task, context, reset_env=True):
        self.reset(task=task, context=context, reset_env=reset_env)
        while True:
            messages, reward, done, info = self.step()
            if done:
                break
        return messages, reward, done, info

    def learn(self, goals=None, reset_env=True):
        self.inventory = []
        self.recorder.elapsed_time = 0
        self.recorder.iteration = 0
        self.step_time = []
        self.critic_agent.last_inventory = "Empty"
        self.critic_agent.last_inventory_used = 0
        with Timer('env reset'):
            self.logger.debug(f'resume: {self.resume}')
            if self.resume:
                # keep the inventory
                self.env.reset(
                    options={
                        "mode": "soft",
                        "wait_ticks": self.env_wait_ticks,
                        "username": self.username
                    }
                )
            else:
                # clear the inventory
                self.env.reset(
                    options={
                        "mode": "hard",
                        "wait_ticks": self.env_wait_ticks,
                        "username": self.username
                    }
                )
                self.resume = True
        self.run_raw_skill("test_env/respawnAndClear.js") # clear inventory without reset
        with Timer('env step empty string'):
            self.last_events = self.env.step("")
        while True:
            if self.recorder.iteration > self.max_iterations:
                self.logger.warning("Iteration limit reached")
                break
            with Timer('planer Agent propose_next_task'):
                task, context = self.planer_agent.propose_next_task(
                    events=self.last_events,
                    environment=self.environment,
                    chest_observation=self.action_agent.render_chest_observation(),
                    goals=goals,
                    max_retries=500,
                )
            self.logger.info(f"Starting task {task} for at most {self.action_agent_task_max_retries} times")
            try:
                with Timer('learn: rollout'):
                    messages, inventory, done, info = self.rollout(
                        task=task,
                        context=context,
                        reset_env=reset_env,
                    )
            except Exception as e:
                time.sleep(3)  # wait for mineflayer to exit
                info = {
                    "task": task,
                    "success": False,
                }
                # reset bot status here
                self.last_events = self.env.reset(
                    options={
                        "mode": "hard",
                        "wait_ticks": self.env_wait_ticks,
                        "inventory": self.last_events[-1][1]["inventory"],
                        "equipment": self.last_events[-1][1]["status"]["equipment"],
                        "position": self.last_events[-1][1]["status"]["position"],
                        "username": self.username
                    }
                )
                # use red color background to print the error
                self.logger.critical(f"Your last round rollout terminated due to error: {e}")
                continue

            # if info["success"]:
            #     self.skill_manager.add_new_skill(info)
            new_inventory = [key for key in inventory if key not in self.inventory]
            self.inventory += new_inventory
            U.f_mkdir(f"./results/{self.environment}")
            U.dump_text(f"Iteration: {self.recorder.iteration}, Inventory obtained: {new_inventory}, Total inventory: {self.inventory}, Num: {len(self.inventory)}\n", f"./results/{self.environment}/{self.action_agent_model_name.replace(' ', '_')}.txt")
            with Timer('Update Exploration Progress'):
                self.planer_agent.update_exploration_progress(info)
            completed = None
            if goals is not None:
                with Timer('Critic Check Goal Success'):
                    completed = self.critic_agent.check_goal_success(self.last_events, self.planer_agent.completed_tasks, self.planer_agent.failed_tasks, goals, mode = "program")
                if completed or self.step_time[-1] >= 36000:
                    break
            self.logger.success(f"Completed tasks: {', '.join(self.planer_agent.completed_tasks)}")
            self.logger.failed(f"Failed tasks: {', '.join(self.planer_agent.failed_tasks)}")
        
        U.f_mkdir(f"./results/{self.environment}")
        self.logger.info(f"\n\nTicks on each step: {self.step_time}, LLM iters: {self.total_iter}, Completed: {completed}")
        U.dump_text(f"\n\nTicks on each step: {self.step_time}; LLM iters: {self.total_iter}; Completed: {completed}", f"./results/{self.environment}/{goals.replace(' ', '_')}{self.action_agent_model_name.replace(' ', '_')}.txt")
        return {
            "completed_tasks": self.planer_agent.completed_tasks,
            "failed_tasks": self.planer_agent.failed_tasks,
            "skills": self.skill_manager.skills,
        }

    def decompose_task(self, task, last_tasklist=None, critique=None, health=None):
        if not self.last_events:
            self.last_events = self.env.reset(
                options={
                    "mode": "hard",
                    "wait_ticks": self.env_wait_ticks,
                    "username": self.username
                }
            )
        return self.planer_agent.decompose_task(self.environment, task, last_tasklist, critique, health)

    def inference(self, task:str=None, sub_goals=[], reset_mode="hard", reset_env=True, feedback_rounds:int=1):
        if not task and not sub_goals:
            raise ValueError("Either task or sub_goals must be provided")
        self.logger.debug(f"Starting inference for task: {task}")
        with Timer('env reset'):
            self.last_events = self.env.reset(
                options={
                    "mode": reset_mode,
                    "wait_ticks": self.env_wait_ticks,
                    "username": self.username
                }
            )
        if not sub_goals:
            with Timer('decompose task'):
                sub_goals = self.decompose_task(task)
                self.logger.debug(f'Decomposed sub_goals: {sub_goals}')
        
        self.planer_agent.completed_tasks = []
        self.planer_agent.failed_tasks = []
        self.last_events = self.env.step("")
        for i in range(feedback_rounds):
            try:
                self.recorder.elapsed_time = 0
                self.recorder.iteration = 0
                self.step_time = []
                self.critic_agent.last_inventory = "Empty"
                self.critic_agent.last_inventory_used = 0
                while self.planer_agent.progress < len(sub_goals):
                    next_task = sub_goals[self.planer_agent.progress]
                    self.logger.debug(f'Next subgoal: {next_task}, All subgoals: {sub_goals}')
                    with Timer('get task context'):
                        context = self.planer_agent.get_task_context(next_task)
                        self.logger.debug(f'Got task context: {context}')
                    with Timer('rollout'):
                        messages, reward, done, info = self.rollout(
                            task=next_task,
                            context=context,
                            reset_env=reset_env,
                        )
                        # self.logger.debug(f'info: {info}')
                    with Timer('Update Exploration Progress'):
                        self.planer_agent.update_exploration_progress(info)
                        self.logger.success(f"Completed tasks: {', '.join(self.planer_agent.completed_tasks)}")
                        self.logger.failed(f"Failed tasks: {', '.join(self.planer_agent.failed_tasks)}")
                    if (self.step_time[-1] >= 24000):
                        self.logger.warning('Inference Time limit reached >=24000')
                        break
                # str_list = task.split()
                # TODO: hard coding
                self.run_raw_skill("test_env/combatEnv.js", [10, 15, 100])
                with Timer('rerank monsters'):
                    combat_order = self.planer_agent.rerank_monster(task=task)
                    self.logger.debug(f'Combat order: {combat_order}')

                for task_item in task.split(','):
                    summon_para = task_item.split()
                    summon_para.insert(1, 5)  # idx =1, r=5
                    self.run_raw_skill("test_env/summonMob.js", summon_para)

                monster_origin = task.split(',')
                try:
                    for monster in combat_order:
                        para = monster.split(' ')
                        combat_para2 = int(para[0])
                        combat_para1 = para[1].lower() # ensure no uppercase
                except:
                    # if error happens, use the origin order to kill monster
                    combat_order = monster_origin
                finally:
                    for monster in combat_order:
                        para = monster.split(' ')
                        combat_para2 = int(para[0])
                        combat_para1 = para[1].lower() # ensure no uppercase
                        with Timer('kill monsters'):
                            self.logger.debug(f'kill monster skill parameter: {combat_para1}, {combat_para2}')
                            kill_res = self.run_raw_skill("skill_library/skill/primitive/killMonsters.js", [combat_para1, combat_para2])
                        if 'lost' in kill_res:
                            break
                
                with Timer('Comment Check Task Success'):
                    health, cirtiques, result, equipment = \
                        self.comment_agent.check_task_success(events=self.last_events, task=sub_goals, time=self.totoal_time, iter=self.total_iter)
                U.f_mkdir(f"./results/{self.environment}")
                U.dump_text(f"Route {i}; Plan list: {sub_goals}; Equipments obtained: {equipment}; Ticks on each step: {self.step_time}; LLM iters: {self.total_iter}; Health: {health:.1f}; Combat result: {result}\n\n", f"./results/{self.environment}/{task.replace(' ', '_')}{self.action_agent_model_name.replace(' ', '_')}.txt")

                with Timer('decompose task again based on feedback'):
                    sub_goals = self.decompose_task(task, last_tasklist=equipment, critique=cirtiques, health=health)
                    self.logger.debug('Decomposed sub_goals based on feedback: {sub_goals}')
                
            except Exception as e:
                U.f_mkdir(f"./results/{self.environment}")
                U.dump_text(f"Route {i}; Plan list: {sub_goals}; Ticks on each step: {self.step_time}; LLM iters: {self.total_iter}; failed; caused by {e}\n\n", f"./results/{self.environment}/{task.replace(' ', '_')}{self.action_agent_model_name.replace(' ', '_')}.txt")
            finally:
                self.run_raw_skill("test_env/respawnAndClear.js")
                self.env.reset(
                    options={
                        "mode": "hard",
                        "wait_ticks": self.env_wait_ticks,
                        "username": self.username
                    }
                )
                self.planer_agent.completed_tasks = []
                self.planer_agent.failed_tasks = []

    def inference_sub_goal(self, task:str=None, sub_goals=[], reset_mode="hard", reset_env=True):
        if not sub_goals:
            raise ValueError("Sub_goals must be provided")
        self.env.reset(
            options={
                "mode": reset_mode,
                "wait_ticks": self.env_wait_ticks,
                "username": self.username
            }
        )
        self.recorder.elapsed_time = 0
        self.recorder.iteration = 0
        self.step_time = []
        self.planer_agent.completed_tasks = []
        self.planer_agent.failed_tasks = []
        self.last_events = self.env.step("")
        self.run_raw_skill("test_env/respawnAndClear.js")
        
        while self.planer_agent.progress < len(sub_goals):
            next_task = sub_goals[self.planer_agent.progress]
            context = self.planer_agent.get_task_context(next_task)
            self.logger.info(f"Starting task {next_task} for at most {self.action_agent_task_max_retries} times")
            messages, reward, done, info = self.rollout(
                task=next_task,
                context=context,
                reset_env=reset_env,
            )
            self.planer_agent.update_exploration_progress(info)
            self.logger.success(f"Completed tasks: {', '.join(self.planer_agent.completed_tasks)}")
            self.logger.failed(f"Failed tasks: {', '.join(self.planer_agent.failed_tasks)}")
            U.f_mkdir(f"./results/{self.environment}")
            if info['success']:
                U.dump_text(f"Subgoal: {next_task}, Ticks: {self.step_time[-1]}\n", f"./results/{self.environment}/{task.replace(' ', '_')}.txt")
            else:
                U.dump_text(f"Subgoal: {next_task}, Ticks: {self.step_time[-1]}, Failed.\n", f"./results/{self.environment}/{task.replace(' ', '_')}.txt")
            if (self.step_time[-1] >= 24000):
                break

    def run_raw_skill(self, skill_path, parameters = [], reset = False):
        # reset here only used for skill test
        if (reset):
            self.env.reset(
                options={
                    "mode": "soft",
                    "wait_ticks": self.env_wait_ticks,
                    "username": self.username
                }
            )
        retry = 3
        while retry > 0:
            try:
                babel = require("@babel/core")
                babel_generator = require("@babel/generator").default

                with open(f"{skill_path}", 'r') as file:
                    code = file.read()

                parsed = babel.parse(code)
                functions = []
                assert len(list(parsed.program.body)) > 0, "No functions found"
                for i, node in enumerate(parsed.program.body):
                    if node.type != "FunctionDeclaration":
                        continue
                    node_type = (
                        "AsyncFunctionDeclaration"
                        if node["async"]
                        else "FunctionDeclaration"
                    )
                    functions.append(
                        {
                            "name": node.id.name,
                            "type": node_type,
                            "body": babel_generator(node).code,
                            "params": list(node["params"]),
                        }
                    )
                # find the last async function
                main_function = None
                for function in reversed(functions):
                    if function["type"] == "AsyncFunctionDeclaration":
                        main_function = function
                        break
                assert (
                    main_function is not None
                ), "No async function found. Your main function must be async."
                assert (
                    main_function["params"][0].name == "bot"
                ), f"Main function {main_function['name']} must take a single argument named 'bot'"
                
                program_code = "\n\n".join(function["body"] for function in functions)
                para_list = "(bot"
                for i in range(len(parameters)):
                    if isinstance(parameters[i], str):
                        para_list += ", " + "\"" + parameters[i] + "\""
                    else:
                        para_list += ", " + str(parameters[i])
                para_list += ");"
                exec_code = f"await {main_function['name']}{para_list}"
                parsed_result = {
                    "program_code": program_code,
                    "program_name": main_function["name"],
                    "exec_code": exec_code,
                }
                break
            except Exception as e:
                retry -= 1
                parsed_result = f"Error parsing action response (before program execution): {e}"

        result = ''
        if isinstance(parsed_result, dict):
            code = parsed_result["program_code"] + "\n" + parsed_result["exec_code"]
            events = self.env.step(
                code,
                programs=self.skill_manager.programs,
            )
            for event in reversed(events):
                if event[0] == 'onChat':
                    result = event[1]['onChat']
                    break
            self.last_events = copy.deepcopy(events)
        else:
            self.logger.warning(f"{parsed_result} Code executes error!")
        
        return result
