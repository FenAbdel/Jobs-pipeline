import os
from pathlib import Path
import configparser


class CongigHandler:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config_path = "part-1/src/config/config.ini"
        self.config.read(self.config_path)

    def get_api_url(self):
        return self.config.get("API", "url")
    
    def get_input_dir(self):
        return self.config.get("Paths", "input_dir")    
    
    def get_registry_file(self):
        return self.config.get("Paths", "registry_file")
     