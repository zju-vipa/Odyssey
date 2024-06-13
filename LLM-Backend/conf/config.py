import json
from pathlib import Path
from typing import Union
CONFIG_PATH = Path(__file__).parent / 'config.json'
class Config():
    def __init__(self) -> None:
        with open(CONFIG_PATH) as f:
            self.config = json.load(f)
            
    def get(self, key:str)->Union[str, None]:
        return self.config.get(key, None)
    
