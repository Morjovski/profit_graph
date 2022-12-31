import json
import os
import datetime
from colorama import init, Fore, Style

class AddData():
    
    def __init__(self, m):
        init(convert=True)
        self.fn = 'data.json'

    def adding_data(self):
        self.d = input(f'Введите дату ({Fore.GREEN}YYYY-MM-DD{Fore.RESET})\n{Fore.RED}Оставьте пустым если дата текущая!{Fore.RESET}: ')
        self.cash = float(input('Введите прибыль наличными за этот день: '))
        self.cashless = float(input('Введите прибыль безналичными за этот день: '))
        if not self.d:
            self.d = str(datetime.datetime.now().date())
        self.dictionary = {"day": self.d, "cash": self.cash, "cashless": self.cashless}
        if os.path.exists(self.fn):
            self.update_file()
        else:
            self.create_file()
    
    def add_many_data(self):
        while True:
            day = input('Введите дату: ')
            if not len(day):
                break
            c = float(input('Введите прибыль наличными: '))
            csh = float(input('Введите прибыль безналичными: '))
            dic = {"day": day, "cash": c, "cashless": csh}
            with open('data.json', 'r+') as f:
                fd = json.load(f)
                f.seek(0)
                fd['data'].append(dic)
                json.dump(fd, f, indent=4)
            print(f'Добавлена прибыль {c + csh} за дату {day}')

    def update_file(self):
        with open(self.fn, 'r+') as f:
            fd = json.load(f)
            f.seek(0)
            fd["data"].append(self.dictionary)
            json.dump(fd, f, indent=4)
            print(f'Прибыль {Fore.GREEN}{self.cash + self.cashless}{Fore.RESET} грн за {Fore.GREEN}{self.d}{Fore.RESET} успешно добавлена!')
            repeat = input('Добавить новую прибыль? (Y/N): ')

    def create_file(self):
        start_file = {"data": [self.dictionary]}
        with open(self.fn, 'w') as f:
            json.dump(start_file, f, indent=4)
            print(f'Файл {Fore.YELLOW}{self.fn}{Fore.RESET} успешно создан с добавлением прибыли {Fore.GREEN}{self.cash + self.cashless}{Fore.RESET} грн за дату {Fore.GREEN}{self.d}{Fore.RESET}!')
