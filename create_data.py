# Запихнуть сюда метод take_period, create_data и equalization из файла graph.py
import json
import datetime
from statistics import mean

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
        '''Optimise dates for next use'''
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
        '''Create data for create_graph bar'''
        self.overall = overall
        self.mode = mode
        if self.overall:
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
            for date in self.file_data['data']:
                if per in date['day']:
                    self.date.append(date['day'])
                    self.profit_cash.append(date['cash'])
                    self.profit_cashless.append(date['cashless'])
                    self.profit.append(round(date['cash'] + date['cashless'], 1))
                    self.purchases.append(date['purchases'])

    def equalization(self, period, mode, overall):
        '''Create data for create_graph_bar'''
        mode_list = []
        if overall:
            overall_sum = 0
            if mode:
                for purchase in self.file_data['data']:
                    if period in purchase['day']:
                        overall_sum += purchase['purchases']
                        mode_list.append(overall_sum)
            else:
                for gain in self.file_data['data']:
                    if period in gain['day']:
                        overall_sum += gain['cash'] + gain['cashless']
                        mode_list.append(overall_sum)
        else:
            if mode:
                for purchase in self.file_data['data']:
                    if period in purchase['day']:
                        mode_list.append(purchase['purchases'])
            else:
                for gain in self.file_data['data']:
                    if period in gain['day']:
                        mode_list.append(gain['cash'] + gain['cashless'])
        '''Generates missing dates if days in month < 31'''
        for i in range(len(mode_list), 31):
            mode_list.append(0)

        return mode_list


    def average(self, info):
        return mean(info)
