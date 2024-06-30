import json
from pathlib import Path
CONFIG_FILE_PATH = Path(__file__).parent.parent.parent / 'conf/config.json'

class ConfigManager:
    def __init__(self):
        with open(CONFIG_FILE_PATH, 'r') as f:
            self.config = json.load(f)

    def __getitem__(self, key):
        return self.get(key)
    
    def get(self, key:str)->str:
        return self.config.get(key, '')