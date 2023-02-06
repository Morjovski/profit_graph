import json
import datetime
from statistics import mean



class CreateData:

    def __init__(self) -> None:
        self.date = []
        self.profit_start = []
        self.profit_end = []
        self.purchases_start = []
        self.purchases_end = []
        self.overall_sum_start = 0
        self.overall_sum_end = 0
        self.overall_list_start = []
        self.overall_list_end = []

    def take_period(self, *periods):
        '''Optimise dates for next use'''

        self.per_first = ['0' + str(i) if len(str(i)) == 0 else str(i) for i in range(1, 32)]
        self.start_period = periods[0]
        self.graph_period_start = datetime.date(int(periods[0][:4]), int(periods[0][5:7]), 1)
        if len(periods) == 2:
            self.end_period = periods[1]
            self.graph_period_end = datetime.date(int(periods[1][:4]), int(periods[1][5:7]), 1)

    def create_data(self, overall, mode):
        '''Create data for create_graph bar'''

        self.overall = overall
        self.mode = mode
        try:
            with open('data.json') as f:
                self.file_data = json.load(f)
        except FileNotFoundError:
            print("There is no 'data.json' file! Enter the data below:")
            self.ad.add_data()

        for info in self.file_data['data']:
            if self.start_period in info['day']:
                self.date.append(info['day'])
                if self.mode:
                    self.overall_sum_start += info['purchases']
                    self.overall_list_start.append(self.overall_sum_start)
                    self.purchases_start.append(info['purchases'])
                else:
                    self.overall_sum_start += info['cash'] + info['cashless']
                    self.overall_list_start.append(round(self.overall_sum_start, 2))
                    self.profit_start.append(round(info['cash'] + info['cashless'], 2))
            try:
                if self.end_period:
                    if self.end_period in info['day']:
                        if self.mode:
                            self.overall_sum_end += info['purchases']
                            self.overall_list_end.append(self.overall_sum_end)
                            self.purchases_end.append(info['purchases'])
                        else:
                            self.overall_sum_end += info['cash'] + info['cashless']
                            self.overall_list_end.append(round(self.overall_sum_end, 2))
                            self.profit_end.append(round(info['cash'] + info['cashless'], 2))                        
            except AttributeError:
                continue

    def equalization(self, mode, overall, period):
        '''Choose right data and generate missing data to create a graph'''

        info_list = []
        if period == self.start_period:
            if overall:
                info_list = self.overall_list_start
            else:
                if mode:
                    info_list = self.purchases_start
                else:
                    info_list = self.profit_start
        else:
            if overall:
                info_list = self.overall_list_end
            else:
                if mode:
                    info_list = self.purchases_end
                else:
                    info_list = self.profit_end
        '''Generates missing dates if days in month less than 31'''
        
        for i in range(len(info_list), 31):
            info_list.append(0)

        return info_list


    def average(self, mode, period):
        '''Return average profit or amout of purchases to create_graph_bar label'''

        info = []
        if period == self.start_period:
            if mode:
                info = self.purchases_start
            else:
                info = self.profit_start
        else:
            if mode:
                info = self.purchases_end
            else:
                info = self.profit_end

        return round(mean(info), 2)