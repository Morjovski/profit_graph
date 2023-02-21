import datetime

import language as lg
import db


class AddData(db.DataBase):
    
    def __init__(self, LANGUAGE):
        self.LANGUAGE = LANGUAGE
        super().__init__()
    
    def add_data(self):
        """Used for adding a new data in SQLite database"""
        while True:
            period, cash, cashless, purchases = AddData.create_answer(self, self.LANGUAGE)
            year, month, day = period[:4], period[5:7], period[8:]

            db.DataBase.create_db(self)
            db.DataBase.insert_year(self, year)
            db.DataBase.insert_month(self, month)
            duplicate = db.DataBase.duplicate_check_db(self, period)
            if duplicate:
                continue
            else:
                db.DataBase.insert_day(self, day, month, cash, cashless, purchases)
            db.DataBase.commit_db(self)
            quit_add_data = int(input('Do you want back to main menu? Leave blank empty if No, else (1) - Yes: '))
            if quit_add_data:
                db.DataBase.close_db(self)
                break
            else:
                continue

    def create_answer(self, LANGUAGE):
        """Collect necessary data"""
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
                        except ValueError:
                            if len(day) == 0:
                                day = datetime.datetime.now().date()
                                print(str(day))
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
