import json
from random import randint
from datetime import datetime
import time

start_time = datetime.now()
date = []
for i in range(1, 1000):
    day = str(randint(1, 31))
    if len(day) == 1:
        day = '0' + day
    month = str(randint(1, 12))
    if len(month) == 1:
        month = '0' + month
    date.append(f'{month}-{day}')
date = sorted(list(set(date)))
with open('data.json', 'r+') as f:
    fd = json.load(f)
    for data in date:
        dic = {"day": f'2022-{data}', "cash": randint(0, 1000), "cashless": randint(0, 1000)}
        f.seek(0)
        fd['data'].append(dic)
    json.dump(fd, f, indent=4)
print(f'Time spend: {datetime.now() - start_time}')