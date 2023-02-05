import json
from random import randint
import os
from datetime import datetime


class RandomData:

    def randomize(self):
        '''Used to create and save random data in data.json'''
        
        start_time = datetime.now()
        fn = 'data.json'
        date = []
        month, day = '', ''
        for intmonth in range(1, 13):
            if len(str(intmonth)) == 1:
                month = '0' + str(intmonth)
            else:
                month = str(intmonth)
            for intday in range(1, 32):
                if len(str(intday)) == 1:
                    day = '0' + str(intday)
                else:
                    day = str(intday)
                date.append(f'2022-{month}-{day}')
        '''If data.json not exist, creates it'''
        if not os.path.exists(fn):
            start_file = {'data': []}
            with open(fn, 'w') as f:
                json.dump(start_file, f, indent=4)

        with open('data.json', 'r+') as f:
            fd = json.load(f)
            for data in date:
                dic = {"day": data, "cash": randint(0, 1000), "cashless": randint(0, 1000), "purchases": randint(1, 100)}
                f.seek(0)
                fd['data'].append(dic)
            json.dump(fd, f, indent=4)
        print(f'Time spend to create and save random data: {datetime.now() - start_time}')
