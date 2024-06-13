import os
import json
from pathlib import Path
CONFIG_FILE_PATH = Path(__file__).parent.parent.parent / 'conf/config.json'
SETENT_EMBEDDING_DEFAULT_DIR = Path(__file__).parent.parent.parent / 'paraphrase-multilingual-MiniLM-L12-v2'
class ConfigManager:
    def __init__(self):
        with open(CONFIG_FILE_PATH, 'r') as f:
            self.config = json.load(f)
        self.config = self.config | {
            'MC_SERVER_HOST': os.getenv('MC_SERVER_HOST', 'localhost'),
            'MC_SERVER_PORT': os.getenv('MC_SERVER_PORT', '25565'),
            'SENTENT_EMBEDDING_DIR': os.getenv('SENTENT_EMBEDDING_DIR', str(SETENT_EMBEDDING_DEFAULT_DIR))
        }

    def __getitem__(self, key):
        return self.get(key)
    
    def get(self, key:str)->str:
        return self.config.get(key, '')