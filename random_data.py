from random import randint
from tqdm import tqdm

import db
import language as lg

class RandomData(db.DataBase):
    
    def __init__(self, LANGUAGE):
        self.LANGUAGE = LANGUAGE

    def randomize(self):
        """Used to create and save random data in data.json"""
        print(lg.randomize_msg_lang[self.LANGUAGE])
        year_step = int(input(lg.random_year_lang[self.LANGUAGE]))
        
        db.DataBase.connect(self)
        db.DataBase.create(self)

        for intyear in tqdm(range(2020, 2020 + year_step + 1)):
            for intmonth in range(1, 13):
                for intday in range(1, 32):
                    day = intday
                    cash = randint(0, 5000)
                    cashless = randint(0, 5000)
                    purchases = randint(0, 500)
                    db.DataBase.insert_year(self, intyear)
                    db.DataBase.insert_month(self, intmonth)
                    db.DataBase.insert_day(self, day, intmonth, cash, cashless, purchases, intyear)
            db.DataBase.commit(self)
        db.DataBase.close(self)