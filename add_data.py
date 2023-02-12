import json
import os
import datetime

from random_data import RandomData
import language as lg

class AddData:
    
    def __init__(self, LANGUAGE):
        self.LANGUAGE = LANGUAGE
    
    def add_data(self):
        '''Used for adding a new data in data.json'''
        while True:
            answ_list = AddData.create_answer(self.LANGUAGE)
            dic = {"day": answ_list[0], "cash": answ_list[1], "cashless": answ_list[2], "purchases": int(answ_list[3])}
            if not os.path.exists(self.fn):
                self.create_file(dic, answ_list[0], answ_list[1], answ_list[2], answ_list[3])
            else:
                self.update_file(dic, answ_list[0], answ_list[1], answ_list[2], answ_list[3])
            
    def update_file(self, dic, day, cash, cashless, purchases):
        '''Update data.json by adding new data'''

        with open('data.json', 'r+') as f:
            fd = json.load(f)
            f.seek(0)
            fd["data"].append(dic)
            json.dump(fd, f, indent=4)
            print(lg.update_file_lang[self.LANGUAGE])
            print()

    def create_file(self, dic, day, cash, cashless, purchases):
        '''Creates data.json if the file not exist then add first data'''
        
        start_file = {"data": [dic]}
        with open('data.json', 'w') as f:
            json.dump(start_file, f, indent=4)
            print(lg.create_file_lang[self.LANGUAGE])
            print()
    
    def create_answer(LANGUAGE):
        enter = lg.create_file_enter_lang[LANGUAGE]
        answ_list = []
        print(lg.enter_quit_add_data_lang[LANGUAGE])
        for index, variable in enumerate(enter):
            if index == 0:
                while True:
                    print(lg.leave_empty_lang[LANGUAGE])
                    day = input(f'{lg.answer_enter_lang[LANGUAGE]} {variable}: ')
                    if day == 'q':
                        AddData.continue_graph(LANGUAGE)
                    else:
                        try:
                            day = datetime.date(int(day[:4]), int(day[5:7]), int(day[8:]))
                        except ValueError as e:
                            if len(day) == 0:
                                day = datetime.datetime.now().date()
                            else:
                                print(lg.incorrect_day_lang[LANGUAGE])
                                continue
                        answ_list.append(str(day))
                        break
            else:
                while True:
                    answ = input(f'{lg.answer_enter_lang[LANGUAGE]} {variable}: ')
                    if answ == 'q':
                        AddData.continue_graph(LANGUAGE)
                    try:
                        answ = float(answ)
                    except ValueError:
                        print(lg.incorrect_data_lang[LANGUAGE])
                        continue
                    answ_list.append(answ)
                    break
        return answ_list

    def continue_graph(LANGUAGE):
        from main import Mode
        n = int(input(f'{lg.back_to_main_menu_lang[LANGUAGE]}'))
        if n:
            mode = Mode()
            mode.select()
        else:
            quit()

