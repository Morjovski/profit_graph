import json
import os
import datetime
import colorama
from colorama import Fore, Style

class AddData():
    
    def __init__(self):
        colorama.init(convert=True)
        self.fn = 'data.json'

    def add_one_data(self):
        '''Used for adding a new data to data.json'''
        self.d = input(f'Введите дату ({Fore.GREEN}YYYY-MM-DD{Fore.RESET})\n{Fore.RED}Оставьте пустым если дата текущая!{Fore.RESET}: ')
        self.cash = float(input('Введите прибыль наличными за день: '))
        self.cashless = float(input('Введите прибыль безналичными за день: '))
        self.purchases = int(input('Введите количество продаж за день: '))
        if not self.d:
            self.d = str(datetime.datetime.now().date())
        self.dictionary = {"day": self.d, "cash": self.cash, "cashless": self.cashless, "purchases": self.purchases}
        if os.path.exists(self.fn):
            self.update_file()
        else:
            self.create_file()
    
    def add_many_data(self):
        '''Used for adding a new data to data.json if data more than 1 day'''
        while True:
            day = input('Введите дату: ')
            if not len(day):
                break
            c = float(input('Введите прибыль наличными: '))
            csh = float(input('Введите прибыль безналичными: '))
            prch = int(input('Введите количество продаж: '))
            dic = {"day": day, "cash": c, "cashless": csh, "purchases": prch}
            with open('data.json', 'r+') as f:
                fd = json.load(f)
                f.seek(0)
                fd['data'].append(dic)
                json.dump(fd, f, indent=4)
            print(f'Добавлена прибыль {c + csh} за дату {day} с {prch} продаж')

    def update_file(self):
        '''Update data.json by adding new data'''
        with open(self.fn, 'r+') as f:
            fd = json.load(f)
            f.seek(0)
            fd["data"].append(self.dictionary)
            json.dump(fd, f, indent=4)
            print(f'{self.purchases} продаж на сумму {Fore.GREEN}{self.cash + self.cashless}{Fore.RESET} грн за {Fore.GREEN}{self.d}{Fore.RESET} успешно добавлена!')

    def create_file(self):
        '''Creates data.json if the file not exist then add first data'''
        start_file = {"data": [self.dictionary]}
        with open(self.fn, 'w') as f:
            json.dump(start_file, f, indent=4)
            print(f'Файл {Fore.YELLOW}{self.fn}{Fore.RESET} успешно создан с добавлением {Fore.GREEN}{self.purchases}{Fore.RESET} продаж на сумму {Fore.GREEN}{self.cash + self.cashless}{Fore.RESET} грн за дату {Fore.GREEN}{self.d}{Fore.RESET}!')
