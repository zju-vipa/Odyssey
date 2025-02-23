import os
import odyssey.utils as U

def load_prompt(prompt):
    package_path = os.getcwd()
    return U.load_text(f"{package_path}/odyssey/prompts/{prompt}.txt")
