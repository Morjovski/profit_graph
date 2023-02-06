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
            answ_list = AddData.create_answer()
            dic = {"day": answ_list[0], "cash": float(answ_list[1]), "cashless": float(answ_list[2]), "purchases": int(answ_list[3])}
            if not os.path.exists(self.fn):
                self.create_file(dic, answ_list[0], answ_list[1], answ_list[2], answ_list[3])
            else:
                self.update_file(dic, answ_list[0], answ_list[1], answ_list[1], answ_list[3])

    def update_file(self, dic, cash, cashless, purchases, day):
        '''Update data.json by adding new data'''

        with open(self.fn, 'r+') as f:
            fd = json.load(f)
            f.seek(0)
            fd["data"].append(dic)
            json.dump(fd, f, indent=4)
            print(f'{purchases} продаж на сумму {Fore.GREEN}{cash + cashless}{Fore.RESET} грн за {Fore.GREEN}{day}{Fore.RESET} успешно добавлена!')
            print()

    def create_file(self, dic, day, cash, cashless, purchases):
        '''Creates data.json if the file not exist then add first data'''
        
        start_file = {"data": [dic]}
        with open(self.fn, 'w') as f:
            json.dump(start_file, f, indent=4)
            print(f'Файл {Fore.YELLOW}{self.fn}{Fore.RESET} успешно создан с добавлением {Fore.GREEN}{purchases}{Fore.RESET} продаж на сумму {Fore.GREEN}{cash + cashless}{Fore.RESET} грн за дату {Fore.GREEN}{day}{Fore.RESET}!')
            print()
    
    def create_answer():
        enter = ['день', 'прибыль наличными', 'прибыль безналичными', 'продажи']
        answ_list = []
        print(f'Введите "{Fore.RED}q{Fore.RESET}" в любой момент для выхода из режима добавления')
        for index, variable in enumerate(enter):
            if index == 0:
                while True:
                    print('Оставьте пустым если дата текущая!')
                    day = input(f'Введите {variable}: ')
                    if day == 'q':
                        quit()
                    try:
                        day = datetime.date(int(day[:4]), int(day[5:7]), int(day[8:]))
                    except ValueError as e:
                        if len(day) == 0:
                            day = datetime.datetime.now().date()
                        else:
                            print(e)
                            continue
                    answ_list.append(day)
                    break
            else:
                while True:
                    answ = input(f'Введите {variable}: ')
                    if answ == 'q':
                        quit()
                    try:
                        answ = float(answ)
                    except ValueError:
                        print('Введено неверное значение!')
                        continue
                    answ_list.append(answ)
                    break
        return answ_list

