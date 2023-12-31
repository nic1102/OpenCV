import datetime
import json


class Logger:
    def __init__(self):
        ...

    @staticmethod
    def send_log(width: int, height: int, file_name: str):
        time = datetime.datetime.now().__str__()
        log = {
            "time": time,
            "width": width,
            "height": height
        }
        with open("logs/"+file_name+".json", "w") as fp:
            json.dump(log, fp)
