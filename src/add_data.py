import datetime
from time import sleep

import language as lg
import db


class AddData(db.DataBase):
    
    def __init__(self, LANGUAGE):
        self.LANGUAGE = LANGUAGE
        super().__init__(self.LANGUAGE)
        self.Flag = False

    def add_data(self):
        """Used for adding a new data in SQLite database"""
        
        self.connect()

        while True:
            try:
                period, cash, cashless, purchases = self._create_answer(self.LANGUAGE)
            except ValueError:
                if self.Flag:
                    self.close()
                    break
            year, month, day = period[:4], period[5:7], period[8:]
            self.create()
            self.insert_year(year)
            self.insert_month(month)
            duplicate = self.duplicate_check(period)
            if duplicate:
                sleep(1)
                continue
            else:
                self.insert_day(day, month, cash, cashless, purchases, year)
                print(lg.success_add_data_lang[self.LANGUAGE])
            self.commit()
            quit_add_data = input(lg.quit_add_data_lang[self.LANGUAGE])
            if not quit_add_data:
                continue
            else:
                self.close()
                break

    def _create_answer(self, LANGUAGE):
        """Collect necessary data"""

        self.Flag = False
        enter = lg.create_file_enter_lang[LANGUAGE]
        answ_list = []
        print(lg.enter_quit_add_data_lang[LANGUAGE])
        for index, variable in enumerate(enter):
            if index == 0:
                while True:
                    print(lg.leave_empty_lang[LANGUAGE])
                    day = input(f'{lg.answer_enter_lang[LANGUAGE]} {variable} {lg.day_format_lang[self.LANGUAGE]}')
                    if day in 'qй':
                        self.Flag = True
                        break
                    else:
                        try:
                            day = datetime.date(int(day[:4]), int(day[5:7]), int(day[8:]))
                        except ValueError:
                            if len(day) == 0:
                                day = datetime.datetime.now().date()
                                print(f"{lg.auto_day_enter_lang[self.LANGUAGE]} {str(day)}")
                            else:
                                print(lg.incorrect_day_lang[LANGUAGE])
                                print(lg.correct_day_format_lang[self.LANGUAGE])
                                sleep(1)
                                continue
                        answ_list.append(str(day))
                        break
            else:
                while True:
                    answ = input(f'{lg.answer_enter_lang[LANGUAGE]} {variable}: ')
                    if answ in 'qй':
                        self.Flag = True
                        break
                    try:
                        if index != 3:
                            answ = float(answ)
                        else:
                            answ = int(answ)
                    except ValueError:
                        print(lg.incorrect_data_lang[LANGUAGE])
                        if index != 3:
                            print(lg.float_value_lang[self.LANGUAGE])
                        else:
                            print(lg.int_value_lang[self.LANGUAGE])
                        sleep(1)
                        continue
                    answ_list.append(answ)
                    break
            if self.Flag:
                break
        return answ_list
