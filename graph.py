import matplotlib.pyplot as plt
import numpy as np
import json
import datetime

class Graph():

    def __init__(self):
        plt.style.use('_mpl-gallery')
        self.date = []
        self.profit_cash = []
        self.profit_cashless = []
        self.profit = []
        self.purchases = []
        with open('data.json') as f:
            self.file_data = json.load(f)

    def take_period(self, *periods):
        try:
            self.start_period = periods[0]
            self.end_period = periods[1]
            self.per_first = ['0' + str(i) if len(str(i)) == 0 else str(i) for i in range(1, 32)]
            # self.per_second = [day['day'] for day in self.file_data['data'] if periods[1] in day['day']]
            # for i in range(len(self.per_first), 31):
            #     self.per_first.append(periods[0] + f'-{i + 1}')
            # for i in range(len(self.per_second), 31):
            #     self.per_first.append(periods[1] + f'-{i + 1}')
            self.graph_period_start = datetime.date(int(periods[0][:4]), int(periods[0][5:7]), 1)
            self.graph_period_end = datetime.date(int(periods[1][:4]), int(periods[1][5:7]), 1)
        except ValueError:
            self.graph_period_end = datetime.date(1970, 1, 1)
        except IndexError:
            self.graph_period_end = datetime.date(int(periods[0][:4]), int(periods[0][5:7]), 1)

    def create_data(self, per):
        # make data
        if per:
            for date in self.file_data['data']:
                if per in date['day']:
                    self.date.append(date['day'])
                    self.profit_cash.append(date['cash'])
                    self.profit_cashless.append(date['cashless'])
                    self.profit.append(date['cash'] + date['cashless'])
                    self.purchases.append(date['purchases'])
        else:
            self.date = [date['day'] for date in self.file_data['data']]
            self.profit = [profit['cash'] + profit['cashless'] for profit in self.file_data['data']]
            self.purchases = [purchases['purchases'] for purchases in self.file_data['data']]

    def create_graph(self, mode):
        # plot
        fig, ax = plt.subplots()
        fig.set_size_inches(10, 8)

        ax.plot(self.date, mode, linewidth=2.0)

        ax.set(xlim=(0, len(self.date) - 1), xticks=np.arange(0, len(self.date)),
            yticks=np.arange(0, (max(mode) + 100 if max(mode) > 100 else max(mode) + 1), (200 if max(mode) > 50 else 1)))

        ax.set_ylabel(('Доход, грн' if max(mode) > 100 else 'Кол-во продаж, шт.'))
        ax.set_xlabel('Дата')
        ax.set_title(f"{('Прибыль за' if max(mode) > 100 else 'Количество продаж за')} {self.graph_period_end.strftime('%B %Y')}")
        plt.setp(ax.get_xticklabels(), rotation=30, ha="right")
        fig.savefig(f"graphs\{('profit' if max(mode) > 100 else 'purchases')}_{self.graph_period_end}.png", bbox_inches='tight')
        plt.show()

    def create_graph_bar(self):
        x = np.arange(len(self.per_first))  # the label locations
        width = 0.35
        fig, ax = plt.subplots()
        fig.set_size_inches(12, 7)
        rects1 = ax.bar(x - width/2, self.equalization(self.start_period), width, label=self.graph_period_start, color = '#279cd6')
        rects2 = ax.bar(x + width/2, self.equalization(self.end_period), width, label=self.graph_period_end, color = '#d62727')

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Доход (грн)')
        ax.set_title(f"Доход за {self.graph_period_start} - {self.graph_period_end}")
        ax.set_xlabel('Дата')
        ax.set_xticks(x, self.per_first)
        ax.legend()

        ax.bar_label(rects1, padding=3)
        ax.bar_label(rects2, padding=3)

        fig.tight_layout()
        plt.setp(ax.get_xticklabels(), rotation=30, ha="right")
        fig.savefig(f"graphs\profit-{self.graph_period_start}_{self.graph_period_end}.png", bbox_inches='tight')

        plt.show()

    def equalization(self, period):
        profit_list = []
        for gain in self.file_data['data']:
            if period in gain['day']:
                profit_list.append(gain['cash'] + gain['cashless'])
        for i in range(len(profit_list), 31):
            profit_list.append(0)
