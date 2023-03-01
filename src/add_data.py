import datetime

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
            period, cash, cashless, purchases = AddData.create_answer(self, self.LANGUAGE)
            year, month, day = period[:4], period[5:7], period[8:]
            if self.Flag:
                self.close()
                break
            self.create()
            self.insert_year(year)
            self.insert_month(month)
            duplicate = self.duplicate_check(period)
            if duplicate:
                continue
            else:
                self.insert_day(day, month, cash, cashless, purchases, year)
            self.commit()
            quit_add_data = input(lg.quit_add_data_lang[self.LANGUAGE])
            if not quit_add_data:
                continue
            else:
                self.close()
                break

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
                        self.Flag = True
                        break
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
                        self.Flag = True
                        break
                    try:
                        answ = float(answ)
                    except ValueError:
                        print(lg.incorrect_data_lang[LANGUAGE])
                        continue
                    answ_list.append(answ)
                    break
            if self.Flag:
                break
        return answ_list
