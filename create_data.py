# Запихнуть сюда метод take_period, create_data и equalization из файла graph.py
import json
import datetime

class CreateData:

    def __init__(self) -> None:
        with open('data.json') as f:
            self.file_data = json.load(f)
        self.date = []
        self.profit_cash = []
        self.profit_cashless = []
        self.profit = []
        self.purchases = []
        self.overall_sum = 0

    def take_period(self, *periods):
        try:
            self.start_period = periods[0]
            self.end_period = periods[1]
            self.per_first = ['0' + str(i) if len(str(i)) == 0 else str(i) for i in range(1, 32)]
            self.graph_period_start = datetime.date(int(periods[0][:4]), int(periods[0][5:7]), 1)
            self.graph_period_end = datetime.date(int(periods[1][:4]), int(periods[1][5:7]), 1)
        except ValueError:
            self.graph_period_end = datetime.date(1970, 1, 1)
        except IndexError:
            self.graph_period_end = datetime.date(int(periods[0][:4]), int(periods[0][5:7]), 1)

    def create_data(self, per, overall, mode):
        self.overall = overall
        self.mode = mode
        # make data
        if per and not self.overall:
            for date in self.file_data['data']:
                if per in date['day']:
                    self.date.append(date['day'])
                    self.profit_cash.append(date['cash'])
                    self.profit_cashless.append(date['cashless'])
                    self.profit.append(round(date['cash'] + date['cashless'], 1))
                    self.purchases.append(date['purchases'])
        elif per and self.overall:
            if self.mode:
                for purchases in self.file_data['data']:
                    if per in purchases['day']:
                        self.date.append(purchases['day'])
                        self.overall_sum += purchases['purchases']
                        self.purchases.append(self.overall_sum)
            else:
                for profit in self.file_data['data']:
                    if per in profit['day']:
                        self.date.append(profit['day'])
                        self.overall_sum += profit['cash'] + profit['cashless']
                        self.profit.append(round(self.overall_sum, 2))                        
        else:
            self.date = [date['day'] for date in self.file_data['data']]
            self.profit = [profit['cash'] + profit['cashless'] for profit in self.file_data['data']]
            self.purchases = [purchases['purchases'] for purchases in self.file_data['data']]

    
    def equalization(self, period):
        profit_list = []
        for gain in self.file_data['data']:
            if period in gain['day']:
                profit_list.append(gain['cash'] + gain['cashless'])
        for i in range(len(self.profit), 31):
            self.profit.append(0)
        return self.profit