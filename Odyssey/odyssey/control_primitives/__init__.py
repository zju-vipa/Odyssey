import os
from pathlib import Path
import odyssey.utils as U


def load_control_primitives(primitive_names=None):
    package_path = Path(__file__).parent.parent
    if primitive_names is None:
        primitive_names = [
            primitives[:-3]
            for primitives in os.listdir(package_path / "control_primitives")
            if primitives.endswith(".js")
        ]
    primitives = [
        U.load_text(str(package_path / "control_primitives" / f"{primitive_name}.js"))
        for primitive_name in primitive_names
    ]
    return primitives
