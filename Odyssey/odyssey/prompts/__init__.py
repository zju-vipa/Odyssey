from pathlib import Path
import odyssey.utils as U


def load_prompt(prompt):
    package_path = Path(__file__).parent.parent
    return U.load_text(str(package_path / "prompts" / f"{prompt}.txt"))
