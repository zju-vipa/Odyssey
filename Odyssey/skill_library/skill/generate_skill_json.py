import os
import json

# this function dumps skills to skill.json
def generate_skill_json(skill_dir):
    skill_json = {}
    code_dir = os.path.join(skill_dir, "compositional")
    description_dir = os.path.join(skill_dir, "description")

    # Iterate through each js file in code directory
    for js_file in os.listdir(code_dir):
        if js_file.endswith(".js"):
            skill_name = os.path.splitext(js_file)[0]
            code_path = os.path.join(code_dir, js_file)
            description_path = os.path.join(description_dir, skill_name + ".txt")
            code_content = read_file_content(code_path)
            description_content = read_file_content(description_path)
            skill_json[skill_name] = {"code": code_content, "description": "Name: " + skill_name + "; Description:" + description_content + "\n"}

    # Write skill.json file
    with open(os.path.join(skill_dir, "skills.json"), "w") as json_file:
        json.dump(skill_json, json_file, indent=4)

def read_file_content(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r", encoding='utf-8') as file:
            return file.read()
    else:
        return ""

if __name__ == "__main__":
    skill_dir = os.path.dirname(os.path.abspath(__file__))
    generate_skill_json(skill_dir)
