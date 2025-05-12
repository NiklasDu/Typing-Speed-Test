import json
import os
from constants import *
from datetime import datetime

class DBHandler():
    def __init__(self):
        pass

    def load_all_user(self): 
        data = []
        if os.path.exists(FILEPATH_USER):
            with open(FILEPATH_USER, "r") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    pass
        all_user = []
        for entry in data:
            all_user.append(entry["user"])
        return all_user

    def add_user(self, user):
        new_user = {
            "user": user
        }
        data = []
        if os.path.exists(FILEPATH_USER):
            with open(FILEPATH_USER, "r") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    pass
        data.append(new_user)
        with open(FILEPATH_USER, "w") as file:
            json.dump(data, file, indent=4)

    def save_result(self, wpm, kpm, total, correct, wrong, user):
        new_result = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "time": datetime.now().strftime("%H:%M"),
            "wpm": round(wpm, 2),
            "kpm": kpm,
            "total": total,
            "correct": correct,
            "wrong": wrong,
            "user": user
        }
        data = []
        if os.path.exists(FILEPATH):
            with open(FILEPATH, "r") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    pass
        data.append(new_result)
        with open(FILEPATH, "w") as f:
            json.dump(data, f, indent=4)
