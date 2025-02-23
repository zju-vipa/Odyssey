import os
import re
import odyssey.utils as U
from langchain.schema import HumanMessage, SystemMessage

from odyssey.prompts import load_prompt
from odyssey.utils.logger import get_logger

class SkillManager:
    def __init__(self):
        # programs for env execution
        self.skill_primitives = self.load_skill_primitives()

    @property
    def programs(self):
        programs = ""
        for primitives in self.skill_primitives:
            programs += f"{primitives}\n\n"
        return programs  
    
    def load_skill_primitives(self, primitive_names=None):
        current_dir = os.getcwd()
        package_path = f"{current_dir}/MCskill/skill"
        if primitive_names is None:
            primitive_names = [
                primitives[:-3]
                for primitives in os.listdir(f"{package_path}")
                if primitives.endswith(".js")
            ]
        primitives = [
            U.load_text(f"{package_path}/{primitive_name}.js")
            for primitive_name in primitive_names
        ]
        return primitives
    
    def render_system_message(self, task_scenario):
        prompt = load_prompt(task_scenario)
        return SystemMessage(content=prompt)
    
    def render_human_message(self, goal_str="", action_str="No current action.", info_str=""):
        content = f"{goal_str}\nCurrent Action: {action_str}\n{info_str}"
        return HumanMessage(content=content)

    def preprocess_func_call_str(self, func_call_str):
        # Preprocess the function call string to replace tuple (x, y, z) with Vec3(x, y, z)
        def replace_tuple_with_vec3(match):
            x, y, z = match.groups()
            return f"new Vec3({x}, {y}, {z})"

        # Preprocess the function call string to replace Python lists with JavaScript arrays
        def replace_python_list_with_js_array(match):
            list_content = match.group(1)
            return f"[{list_content}]"

        # Use regex to find tuples like (x, y, z) and replace with Vec3(x, y, z)
        func_call_str = re.sub(r"\((\d+),\s*(\d+),\s*(\d+)\)", replace_tuple_with_vec3, func_call_str)

        # Use regex to find Python lists like [a, b, c] and replace with JavaScript arrays
        func_call_str = re.sub(r"\[([^\]]+)\]", replace_python_list_with_js_array, func_call_str)

        return func_call_str
