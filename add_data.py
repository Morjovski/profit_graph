import json
import os
import datetime
import colorama
from colorama import Fore


class AddData:
    
    def __init__(self):
        colorama.init(convert=True)
        self.fn = 'data.json'
    
    def add_data(self):
        '''Used for adding a new data in data.json'''

        while True:
            print(f'Введите "{Fore.RED}q{Fore.RESET}" для выхода из режима добавления')
            day = input(f'Введите дату ({Fore.GREEN}YYYY-MM-DD{Fore.RESET}): ')
            if day.lower() == 'q':
                break            
            if not day:
                day = str(datetime.datetime.now().date())
            cash = float(input('Введите прибыль наличными: '))
            cashless = float(input('Введите прибыль безналичными: '))
            purchases = int(input('Введите количество продаж: '))
            dic = {"day": day, "cash": cash, "cashless": cashless, "purchases": purchases}
            if not os.path.exists(self.fn):
                self.create_file(dic, cash, cashless, purchases, day)
            else:
                self.update_file(dic, cash, cashless, purchases, day)

    def update_file(self, dic, cash, cashless, purchases, day):
        '''Update data.json by adding new data'''

        with open(self.fn, 'r+') as f:
            fd = json.load(f)
            f.seek(0)
            fd["data"].append(dic)
            json.dump(fd, f, indent=4)
            print(f'{purchases} продаж на сумму {Fore.GREEN}{cash + cashless}{Fore.RESET} грн за {Fore.GREEN}{day}{Fore.RESET} успешно добавлена!')
            print()

    def create_file(self, dic, cash, cashless, purchases, day):
        '''Creates data.json if the file not exist then add first data'''
        
        start_file = {"data": [dic]}
        with open(self.fn, 'w') as f:
            json.dump(start_file, f, indent=4)
            print(f'Файл {Fore.YELLOW}{self.fn}{Fore.RESET} успешно создан с добавлением {Fore.GREEN}{purchases}{Fore.RESET} продаж на сумму {Fore.GREEN}{cash + cashless}{Fore.RESET} грн за дату {Fore.GREEN}{day}{Fore.RESET}!')
            print()
