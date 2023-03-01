import json


class Data:
    def __init__(self, path):
        self.path = path

    def get_data(self):
        with open(self.path) as f:
            return json.load(f)



