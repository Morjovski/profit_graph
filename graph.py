import matplotlib.pyplot as plt
import numpy as np
import json

class Graph():

    def __init__(self, m):
        plt.style.use('_mpl-gallery')
        self.date = []
        self.profit = []

    def create_data(self, per):
        with open('data.json') as f:
            file_data = json.load(f)
        # make data
        if per:
            for date in file_data['data']:
                if per in date['day']:
                    self.date.append(date['day'])
                    self.profit.append(date['cash'] + date['cashless'])
        else:
            self.date = [date['day'] for date in file_data['data']]
            self.profit = [profit['cash'] + profit['cashless'] for profit in file_data['data']]

    def create_graph(self):
        # plot
        fig, ax = plt.subplots()

        ax.plot(self.date, self.profit, linewidth=2.0)

        ax.set(xlim=(0, len(self.date) - 1), xticks=np.arange(0, len(self.date)),
            yticks=np.arange(0, max(self.profit) + 100, 100))

        ax.set_ylabel('Доход, грн')
        ax.set_xlabel('Дата')
        ax.set_title('Прибыль за отрезок времени')
        plt.setp(ax.get_xticklabels(), rotation=30, ha="right")

        plt.show()