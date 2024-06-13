import pkg_resources
import odyssey.utils as U


def load_prompt(prompt):
    package_path = pkg_resources.resource_filename("odyssey", "")
    return U.load_text(f"{package_path}/prompts/{prompt}.txt")
