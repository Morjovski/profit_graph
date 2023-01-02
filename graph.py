import matplotlib.pyplot as plt
import numpy as np
import json
import datetime
class Graph():

    def __init__(self, m):
        plt.style.use('_mpl-gallery')
        self.date = []
        self.profit_cash = []
        self.profit_cashless = []
        self.profit = []
        self.purchases = []

    def create_data(self, per):
        self.graph_period = datetime.date(int(per[:4]), int(per[5:7]), 1)
        with open('data.json') as f:
            file_data = json.load(f)
        # make data
        if per:
            for date in file_data['data']:
                if per in date['day']:
                    self.date.append(date['day'])
                    self.profit_cash.append(date['cash'])
                    self.profit_cashless.append(date['cashless'])
                    self.profit.append(date['cash'] + date['cashless'])
                    try:
                        self.purchases.append(date['purchases'])
                    except:
                        continue
        else:
            self.date = [date['day'] for date in file_data['data']]
            self.profit = [profit['cash'] + profit['cashless'] for profit in file_data['data']]
            # try:
            #     self.purchases = [purchases['purchases'] for purchases in file_data['data']]
            # except:
            #     self.purchases = []

    def create_graph(self):
        # plot
        fig, ax = plt.subplots()
        fig.set_size_inches(10, 8)

        ax.plot(self.date, self.profit, linewidth=2.0)

        ax.set(xlim=(0, len(self.date) - 1), xticks=np.arange(0, len(self.date)),
            yticks=np.arange(0, max(self.profit) + 100, 200))

        ax.set_ylabel('Доход, грн')
        ax.set_xlabel('Дата')
        ax.set_title(f"Прибыль за {self.graph_period.strftime('%B %Y')}")
        plt.setp(ax.get_xticklabels(), rotation=30, ha="right")
        print(self.graph_period)
        fig.savefig(f"graphs\graph_{self.graph_period}.png", bbox_inches='tight')
        plt.show()

    def create_graph_bar(self):
        x = np.arange(len(self.date))  # the label locations
        width = 0.35
        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width/2, self.profit_cash, width, label='Наличка', color = '#279cd6')
        rects2 = ax.bar(x + width/2, self.profit_cashless, width, label='Безналичный', color = '#d62727')

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Доход (грн)')
        ax.set_title('Наличный\безналичный доход за отрезок времени')
        ax.set_xticks(x, self.date)
        ax.legend()

        ax.bar_label(rects1, padding=3)
        ax.bar_label(rects2, padding=3)

        fig.tight_layout()
        plt.setp(ax.get_xticklabels(), rotation=30, ha="right")

        plt.show()