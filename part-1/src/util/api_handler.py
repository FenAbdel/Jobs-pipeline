from datetime import datetime
import os
import requests
from util.config_handler import CongigHandler

class ApiHandler:
    def __init__(self):
        self.config_handler = CongigHandler()
        self.api_url = self.config_handler.get_api_url()
        self.input_dir = self.config_handler.get_input_dir()
        
    def get_data_to_csv(self):
        print("[INFO] Getting data from API...")
        request = requests.get(self.api_url)
        if request.status_code == 200:
            data = request.text
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            file_path = f"JOBS_{timestamp}.csv"
            file_path = os.path.join(self.input_dir, file_path)
            with open(file_path, "w",newline="",encoding="utf-8") as csvfile:
                csvfile.write(data)
            print(f"[INFO] Data saved in {file_path}")
        else:
            print("[ERROR] API request failed")
        