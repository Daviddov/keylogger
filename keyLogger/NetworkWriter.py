import json
import requests
from IWrite import IWrite

class NetworkWrite(IWrite):
    def __init__(self, config_path="config.json"):
        self.url = self.load_config(config_path)

    def load_config(self, config_path):
        """טוען את כתובת ה-URL מקובץ ה-config"""
        try:
            with open(config_path, "r", encoding="utf-8") as file:
                config = json.load(file)
                return config.get("url", "http://127.0.0.1:5000/api")  # ברירת מחדל אם חסר
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading config: {e}")
            return "http://127.0.0.1:5000/api"  # כתובת ברירת מחדל במקרה של שגיאה

    def Write(self, data):
        """שליחת הנתונים לרשת"""
        print("Writing to network...")
        headers = {"Content-Type": "application/json"}  # חובה להגדיר כ- JSON

        try:
            response = requests.post(self.url, json=data, headers=headers)  # שימוש ב- json=data
            if response.status_code == 200:
                print(response.json())
            else:
                print(f"Failed to send data: {response.status_code} - {response.text}")
        except requests.RequestException as e:
            print(f"Network error: {e}")

if __name__ == '__main__':
    data = {"key": "value"}  # מבנה JSON תקין
    nw = NetworkWrite()
    nw.Write(data)
