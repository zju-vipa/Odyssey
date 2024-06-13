import re
import time

import odyssey.utils as U
from odyssey.utils.json_utils import fix_and_parse_json
from javascript import require
from langchain.schema import AIMessage, HumanMessage, SystemMessage

from odyssey.prompts import load_prompt
from odyssey.control_primitives_context import load_control_primitives_context
from odyssey.utils.logger import get_logger

class ActionAgent:
    def __init__(
        self,
        request_timout=120,
        ckpt_dir="ckpt",
        resume=False,
        chat_log=True,
        execution_error=True,
    ):
        self.ckpt_dir = ckpt_dir
        self.chat_log = chat_log
        self.execution_error = execution_error
        self.logger = get_logger("ActionAgent")
        U.f_mkdir(f"{ckpt_dir}/action")
        if resume:
            self.logger.info(f"Loading Action Agent from {ckpt_dir}/action")
            self.chest_memory = U.load_json(f"{ckpt_dir}/action/chest_memory.json")
        else:
            self.chest_memory = {}

    def update_chest_memory(self, chests):
        for position, chest in chests.items():
            if position in self.chest_memory:
                if isinstance(chest, dict):
                    self.chest_memory[position] = chest
                if chest == "Invalid":
                    self.logger.debug(f"Removing chest {position}: {chest}")
                    self.chest_memory.pop(position)
            else:
                if chest != "Invalid":
                    self.logger.debug(f"Saving chest {position}: {chest}")
                    self.chest_memory[position] = chest
        U.dump_json(self.chest_memory, f"{self.ckpt_dir}/action/chest_memory.json")

    def render_chest_observation(self):
        chests = []
        for chest_position, chest in self.chest_memory.items():
            if isinstance(chest, dict) and len(chest) > 0:
                chests.append(f"{chest_position}: {chest}")
        for chest_position, chest in self.chest_memory.items():
            if isinstance(chest, dict) and len(chest) == 0:
                chests.append(f"{chest_position}: Empty")
        for chest_position, chest in self.chest_memory.items():
            if isinstance(chest, str):
                assert chest == "Unknown"
                chests.append(f"{chest_position}: Unknown items inside")
        assert len(chests) == len(self.chest_memory)
        if chests:
            chests = "\n".join(chests)
            return f"Chests:\n{chests}\n\n"
        else:
            return f"Chests: None\n\n"

    def render_system_message(self):
        system_message =  SystemMessage(content=load_prompt("action_template"))
        # FIXME: Hardcoded control_primitives
        # base_skills = [
        #     "exploreUntil",
        #     "mineBlock",
        #     "craftItem",
        #     "placeItem",
        #     "smeltItem",
        #     "killMob",
        # ]
        # if not self.llm.model_name == "gpt-3.5-turbo":
        #     base_skills += [
        #         "useChest",
        #         "mineflayer",
        #     ]
        # programs = "\n\n".join(load_control_primitives_context(base_skills) + skills)
        # response_format = load_prompt("action_response_format")
        # system_message_prompt = SystemMessagePromptTemplate.from_template(
        #     system_template
        # )
        # system_message = system_message_prompt.format()
        assert isinstance(system_message, SystemMessage)
        return system_message

    def render_human_message(
        self, *, events, code="", task="", context="", critique="", skills=""
    ):
        chat_messages = []
        error_messages = []
        # FIXME: damage_messages is not used
        damage_messages = []
        assert events[-1][0] == "observe", "Last event must be observe"
        for i, (event_type, event) in enumerate(events):
            if event_type == "onChat":
                chat_messages.append(event["onChat"])
            elif event_type == "onError":
                error_messages.append(event["onError"])
            elif event_type == "onDamage":
                damage_messages.append(event["onDamage"])
            elif event_type == "observe":
                biome = event["status"]["biome"]
                time_of_day = event["status"]["timeOfDay"]
                voxels = event["voxels"]
                entities = event["status"]["entities"]
                health = event["status"]["health"]
                hunger = event["status"]["food"]
                position = event["status"]["position"]
                equipment = event["status"]["equipment"]
                inventory_used = event["status"]["inventoryUsed"]
                inventory = event["inventory"]
                assert i == len(events) - 1, "observe must be the last event"

        observation = ""

        if code:
            observation += f"Program used in the last round:\n{code}\n\n"
        else:
            observation += f"Program used in the last round: None\n\n"

        programs = "".join(skills)
        observation += f"Task: {task}\n\n"
        observation += f"Programs: {programs}"

        if critique:
            observation += f"Critique: {critique}\n\n"
        else:
            observation += f"Critique: None\n\n"

        return HumanMessage(content=observation)

    def process_ai_message(self, message, skills):
        assert isinstance(message, AIMessage)

        retry = 3
        error = None
        while retry > 0:
            try:
                babel = require("@babel/core")
                babel_generator = require("@babel/generator").default

                code_pattern = re.compile(r"{(.*?)}", re.DOTALL)
                code_name = "".join(code_pattern.findall(message.content)[0])
                action = "{" + code_name + "}"
                action_resp = fix_and_parse_json(action)
                assert "program" in action_resp
                code_name = action_resp['program']
                self.logger.debug(f'code name: {code_name}')

                code = [c for c in skills if code_name in c]
                if len(code) == 0:
                    code = [skills[0]]
                parsed = babel.parse(code[0])
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
                    len(main_function["params"]) == 1
                    and main_function["params"][0].name == "bot"
                ), f"Main function {main_function['name']} must take a single argument named 'bot'"
                program_code = "\n\n".join(function["body"] for function in functions)
                exec_code = f"await {main_function['name']}(bot);"
                return {
                    "program_code": program_code,
                    "program_name": main_function["name"],
                    "exec_code": exec_code,
                }
            except Exception as e:
                retry -= 1
                error = e
                self.logger.warning(e)
                time.sleep(1)
        return f"Error parsing action response (before program execution): {error}"

    def summarize_chatlog(self, events):
        def filter_item(message: str):
            craft_pattern = r"I cannot make \w+ because I need: (.*)"
            craft_pattern2 = (
                r"I cannot make \w+ because there is no crafting table nearby"
            )
            mine_pattern = r"I need at least a (.*) to mine \w+!"
            if re.match(craft_pattern, message):
                return re.match(craft_pattern, message).groups()[0]
            elif re.match(craft_pattern2, message):
                return "a nearby crafting table"
            elif re.match(mine_pattern, message):
                return re.match(mine_pattern, message).groups()[0]
            else:
                return ""

        chatlog = set()
        for event_type, event in events:
            if event_type == "onChat":
                item = filter_item(event["onChat"])
                if item:
                    chatlog.add(item)
        return "I also need " + ", ".join(chatlog) + "." if chatlog else ""
