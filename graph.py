import matplotlib.pyplot as plt
import numpy as np
import datetime
from statistics import mean

from open_file import OpenDataFile


class Graph(OpenDataFile):

    def __init__(self):
        super().__init__()
        plt.style.use('_mpl-gallery')
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

    def create_graph(self, pur_or_pro):
        # plot
        fig, ax = plt.subplots()
        fig.set_size_inches(10, 8)

        ax.plot(self.date, pur_or_pro, linewidth=2.0)
        if self.overall:
            ax.set(xlim=(0, len(self.date) - 1), xticks=np.arange(0, len(self.date)),
                yticks=np.arange(0, (max(pur_or_pro) + 1000 if max(pur_or_pro) > 5000 else max(pur_or_pro) + 10), (1000 if max(pur_or_pro) > 1000 else 10)))
        else:
            ax.set(xlim=(0, len(self.date) - 1), xticks=np.arange(0, len(self.date)),
                yticks=np.arange(0, (max(pur_or_pro) + 100 if max(pur_or_pro) > 100 else max(pur_or_pro) + 1), (200 if max(pur_or_pro) > 50 else 1)))

        ax.set_ylabel(('Доход, грн' if max(pur_or_pro) > 1000 else 'Кол-во продаж, шт.'))
        ax.set_xlabel('Дата')
        ax.set_title(f"{('Прибыль за' if max(pur_or_pro) > 1000 else 'Количество продаж за')} {self.graph_period_end.strftime('%B %Y')}")
        for index in range(len(self.date)):
            if index % 2 == 0:
                ax.text(self.date[index], pur_or_pro[index], pur_or_pro[index], size=12)
        ax.text(self.date[-1], pur_or_pro[-1], pur_or_pro[-1], size=12)
        plt.setp(ax.get_xticklabels(), rotation=30, ha="right")
        plt.plot(pur_or_pro, marker='o', mec = 'r', mfc = 'r')
        fig.savefig(f"graphs\{('profit' if max(pur_or_pro) > 1000 else 'purchases')}_{self.graph_period_end}.png", bbox_inches='tight')
        plt.show()

    def create_graph_bar(self, mode, overall):

        start_period = self.equalization(self.start_period, mode, overall)
        end_period = self.equalization(self.end_period, mode, overall)
        max_value = max(max(start_period), max(end_period))

        x = np.arange(len(self.per_first))  # the label locations
        width = 0.45
        fig, ax = plt.subplots()
        fig.set_size_inches(15, 10)

        rects1 = ax.bar(x - width/2, start_period, width, label=self.graph_period_start.strftime('%B %Y'), color = '#279cd6')
        rects2 = ax.bar(x + width/2, end_period, width, label=self.graph_period_end.strftime('%B %Y'), color = '#d62727')

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Продажи (шт.)' if mode else 'Доход (грн)')
        ax.set_title(f"Продажи за {self.graph_period_start.strftime('%B %Y')} - {self.graph_period_end.strftime('%B %Y')}"
                     if mode else f"Доход за {self.graph_period_start.strftime('%B %Y')} - {self.graph_period_end.strftime('%B %Y')}")
        ax.set_xlabel('Дата')
        ax.set_xticks(x, self.per_first)

        if mode:
            if overall:
                ax.set_yticks(np.arange(0, (max_value // 100) * 100 + 200, 50))
            else:
                ax.set_yticks(np.arange(0, (max_value // 10) * 10 + 20, 5))
        else:
            if overall:
                ax.set_yticks(np.arange(0, (max_value // 10000) * 10000 + 20000, 5000))
            else:
                ax.set_yticks(np.arange(0, (max_value // 1000) * 1000 + 2000, 500))

        ax.legend(loc=2)

        ax.bar_label(rects1, fontsize=10, rotation=90, weight='bold', label_type='edge', color='black', padding=10)
        ax.bar_label(rects2, fontsize=10, rotation=90, weight='bold', label_type='edge', color='black', padding=10)
        fig.tight_layout()
        # plt.setp(ax.get_xticklabels())
        if mode:
            fig.savefig(f"graphs\purchases_{self.graph_period_start.strftime('%B %Y')}-{self.graph_period_end.strftime('%B %Y')}.png", bbox_inches='tight')
        else:
            fig.savefig(f"graphs\profit_{self.graph_period_start.strftime('%B %Y')}-{self.graph_period_end.strftime('%B %Y')}.png", bbox_inches='tight')
        plt.show()

    def equalization(self, period, mode, overall):
        mode_list = []
        if overall:
            overall_sum = 0
            if not mode:
                for gain in self.file_data['data']:
                    if period in gain['day']:
                        overall_sum += gain['cash'] + gain['cashless']
                        mode_list.append(overall_sum)
            else:
                for purchase in self.file_data['data']:
                    if period in purchase['day']:
                        overall_sum += purchase['purchases']
                        mode_list.append(overall_sum)
        else:
            if not mode:
                for gain in self.file_data['data']:
                    if period in gain['day']:
                        mode_list.append(gain['cash'] + gain['cashless'])
            else:
                for purchase in self.file_data['data']:
                    if period in purchase['day']:
                        mode_list.append(purchase['purchases'])

        for i in range(len(mode_list), 31):
            mode_list.append(0)

        return mode_list
