import matplotlib.pyplot as plt
import numpy as np
from create_data import CreateData
import mplcursors

import language as lg


class Graph(CreateData):

    def __init__(self, LANGUAGE):
        self.LANGUAGE = LANGUAGE
        super().__init__(LANGUAGE)
        plt.style.use('_mpl-gallery')
        self.first_color = '#2D2926FF'
        self.second_color = '#E94B3CFF'
        plt.rcParams["figure.autolayout"] = True

    def create_graph(self, pur_or_pro):
        '''Create one period graph by days in plot(x, y) style'''

        fig, ax = plt.subplots()
        fig.set_size_inches(10, 8)

        dt = plt.scatter(self.date, pur_or_pro, c=self.second_color, marker='o', label=f'Среднее значение: {self.average(self.mode, self.start_period)}')

        if self.overall:
            if max(pur_or_pro) <= 100:
                ax.set(xlim=(0, len(self.date) - 1), xticks=np.arange(0, len(self.date)),
                    yticks=np.arange(0, max(pur_or_pro) + 10, 1))
            elif max(pur_or_pro) <= 500:
                ax.set(xlim=(0, len(self.date) - 1), xticks=np.arange(0, len(self.date)),
                    yticks=np.arange(0, max(pur_or_pro) + 25, 25))
            elif max(pur_or_pro) <= 5000:
                ax.set(xlim=(0, len(self.date) - 1), xticks=np.arange(0, len(self.date)),
                    yticks=np.arange(0, max(pur_or_pro) + 100, 250))
            else:
                ax.set(xlim=(0, len(self.date) - 1), xticks=np.arange(0, len(self.date)),
                    yticks=np.arange(0, max(pur_or_pro) + 1000, 2500))
        else:
            ax.set(xlim=(0, len(self.date) - 1), xticks=np.arange(0, len(self.date)),
                yticks=np.arange(0, (max(pur_or_pro) + 100 if max(pur_or_pro) > 100 else max(pur_or_pro) + 1), (200 if max(pur_or_pro) > 50 else 1)))

        ax.set_ylabel((lg.profit_label_lang[self.LANGUAGE] if max(pur_or_pro) > 1000 else lg.purchases_label_lang[self.LANGUAGE]))
        ax.set_xlabel(lg.hover_annotation_day_lang[self.LANGUAGE])
        ax.set_title(f"{lg.profit_title_lang[self.LANGUAGE] if max(pur_or_pro) > 1000 else lg.purchases_title_lang[self.LANGUAGE]}) {self.graph_period_start.strftime('%B %Y')}")

        ax.legend(loc=2)

        plt.setp(ax.get_xticklabels(), rotation=30, ha="right")

        cursor = mplcursors.cursor(dt, hover='True')
        @cursor.connect("add")
        def on_add(sel):
            xi, yi = sel.target
            xi = int(round(xi))
            sel.annotation.set_text(f'{lg.hover_annotation_day_lang[self.LANGUAGE]}: {self.date[xi]}\n{lg.hover_annotation_value_lang[self.LANGUAGE]} {yi}')
            sel.annotation.get_bbox_patch().set(fc='#F2EDD7FF', alpha=0.6)

        plt.plot(self.date, pur_or_pro, color=self.first_color, alpha=0.5)

        fig.savefig(f"graphs/{('profit' if max(pur_or_pro) > 1000 else 'purchases')}_{self.graph_period_start}.png", bbox_inches='tight')
        plt.show()

    def create_graph_bar(self, mode, overall):
        '''Compare two periods by grouped bar chart style'''
        
        start_period = self.equalization(mode, overall, self.start_period)
        end_period = self.equalization(mode, overall, self.end_period)
        max_value = max(max(start_period), max(end_period))

        if mode:
            label_start = f"{self.graph_period_start.strftime('%B %Y')}, {lg.average_purchases_lang[self.LANGUAGE]} {self.average(self.mode, self.start_period)}"
            label_end = f"{self.graph_period_end.strftime('%B %Y')}, {lg.average_purchases_lang[self.LANGUAGE]} {self.average(self.mode, self.end_period)}"
        else:
            label_start = f"{self.graph_period_start.strftime('%B %Y')}, {lg.average_profit_lang[self.LANGUAGE]} {self.average(self.mode, self.start_period)}"
            label_end = f"{self.graph_period_end.strftime('%B %Y')}, {lg.average_profit_lang[self.LANGUAGE]} {self.average(self.mode, self.end_period)}"

        x = np.arange(len(self.per_first))
        width = 0.45
        fig, ax = plt.subplots()
        fig.set_size_inches(15, 10)

        rects1 = ax.bar(x - width/2, start_period, width, label=label_start, color = self.first_color)
        rects2 = ax.bar(x + width/2, end_period, width, label=label_end, color = self.second_color)

        ax.set_ylabel(lg.purchases_label_lang[self.LANGUAGE] if mode else lg.profit_label_lang[self.LANGUAGE])
        ax.set_title(f"{lg.purchases_title_lang[self.LANGUAGE]} {self.graph_period_start.strftime('%B %Y')} - {self.graph_period_end.strftime('%B %Y')}"
                     if mode else f"{lg.profit_title_lang[self.LANGUAGE]} {self.graph_period_start.strftime('%B %Y')} - {self.graph_period_end.strftime('%B %Y')}")
        ax.set_xlabel(lg.hover_annotation_day_lang[self.LANGUAGE])
        ax.set_xticks(x, self.per_first)

        if mode:
            if overall:
                ax.set_yticks(np.arange(0, (max_value // 100) * 100 + 200, 50))
            else:
                ax.set_yticks(np.arange(0, (max_value // 10) * 10 + 20, 5))
        else:
            if overall:
                ax.set_yticks(np.arange(0, (max_value // 10000) * 10000 + 20000, 2500))
            else:
                ax.set_yticks(np.arange(0, (max_value // 1000) * 1000 + 2000, 500))

        ax.legend(loc=2)

        fig.tight_layout()

        cursor = mplcursors.cursor([rects1, rects2], hover='True')
        @cursor.connect("add")
        def on_add(sel):
            x, y, width, height = sel.artist[sel.index].get_bbox().bounds
            sel.annotation.set(text=f'{lg.hover_annotation_day_lang[self.LANGUAGE]}: {self.per_first[sel.index]}\n{lg.hover_annotation_value_lang[self.LANGUAGE]} {height}', position=(0, 20), anncoords="offset points")
            sel.annotation.xy = (x + width / 2, y + height)
            sel.annotation.get_bbox_patch().set(fc='#F2EDD7FF', alpha=0.6)
            
        if mode:
            fig.savefig(f"graphs/purchases_{self.graph_period_start.strftime('%B %Y')}-{self.graph_period_end.strftime('%B %Y')}.png", bbox_inches='tight')
        else:
            fig.savefig(f"graphs/profit_{self.graph_period_start.strftime('%B %Y')}-{self.graph_period_end.strftime('%B %Y')}.png", bbox_inches='tight')
        plt.show()
