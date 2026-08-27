import os
from pathlib import Path
import odyssey.utils as U


def load_control_primitives_context(primitive_names=None):
    package_path = Path(__file__).parent.parent
    if primitive_names is None:
        primitive_names = [
            primitive[:-3]
            for primitive in os.listdir(package_path / "control_primitives_context")
            if primitive.endswith(".js")
        ]
    primitives = [
        U.load_text(str(package_path / "control_primitives_context" / f"{primitive_name}.js"))
        for primitive_name in primitive_names
    ]
    return primitives
