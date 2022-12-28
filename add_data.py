import json
import os

class AddData():
    
    def __init__(self, m):
        self.fn = 'data.json'

    def adding(self):
        self.d = input('Введите дату: ')
        self.p = int(input('Введите прибыль за этот день: '))
        self.dictionary = {"day": self.d, "profit": self.p}
        if os.path.exists(self.fn):
            self.update_file()
        else:
            self.create_file()
        
    def update_file(self):
        with open(self.fn, 'r+') as f:
            fd = json.load(f)
            f.seek(0)
            fd["data"].append(self.dictionary)
            json.dump(fd, f, indent=4)

    def create_file(self):
        start_file = {"data": [self.dictionary]}
        with open(self.fn, 'w') as f:
            json.dump(start_file, f, indent=4)
