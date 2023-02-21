import matplotlib.pyplot as plt
import matplotlib.ticker as tic
import numpy as np
import mplcursors

from create_data import CreateData
import language as lg


class Graph(CreateData):

    def __init__(self, LANGUAGE):
        self.LANGUAGE = LANGUAGE
        super().__init__(LANGUAGE)
        plt.style.use('_mpl-gallery')
        self.colors = ['#82776e', '#776d65', '#6d635c', '#625953', '#58504a', '#4d4641', '#423c38',
                       '#38332f', '#2d2926', '#221f1d', '#181614', '#0d0c0b', '#020202']
        plt.rcParams["figure.autolayout"] = True

    def create_graph_bar(self, formatted_list):
        """Compare two periods by grouped bar chart style"""
        
        # start_period = self.equalization(mode, overall, self.start_period)
        # end_period = self.equalization(mode, overall, self.end_period)
        # max_value = self.max_data(formatted_list)
        fig, ax = plt.subplots()
        # fig.set_size_inches(15, 10)
        colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
        n_bars = len(formatted_list)
        if n_bars < 3:
            total_width = 0.5
        else:
            total_width = 0.8
        bar_width = total_width / n_bars
        bars = []
        for index, (name, values) in enumerate(formatted_list.items()):
            x_offset = (index - n_bars / 2) * bar_width + bar_width / 2
            for x, y in enumerate(values):
                bar = ax.bar(x + x_offset, y, width=bar_width * 0.8, color=self.colors[index % len(colors)])
            bars.append(bar[0])
        ax.legend(bars, formatted_list.keys())


        # if mode:
        #     label_start = f"{self.graph_period_start.strftime('%B %Y')}, {lg.average_purchases_lang[self.LANGUAGE]} {self.average(self.mode, self.start_period)}"
        #     label_end = f"{self.graph_period_end.strftime('%B %Y')}, {lg.average_purchases_lang[self.LANGUAGE]} {self.average(self.mode, self.end_period)}"
        # else:
        #     label_start = f"{self.graph_period_start.strftime('%B %Y')}, {lg.average_profit_lang[self.LANGUAGE]} {self.average(self.mode, self.start_period)}"
        #     label_end = f"{self.graph_period_end.strftime('%B %Y')}, {lg.average_profit_lang[self.LANGUAGE]} {self.average(self.mode, self.end_period)}"

        # rects1 = ax.bar(x - width/2, start_period, width, label=label_start, color = self.first_color)
        # rects2 = ax.bar(x + width/2, end_period, width, label=label_end, color = self.second_color)

        # ax.set_title(f"{lg.purchases_title_lang[self.LANGUAGE]} {self.graph_period_start.strftime('%B %Y')} - {self.graph_period_end.strftime('%B %Y')}"
        #              if mode else f"{lg.profit_title_lang[self.LANGUAGE]} {self.graph_period_start.strftime('%B %Y')} - {self.graph_period_end.strftime('%B %Y')}")
        # ax.set_ylabel(lg.purchases_label_lang[self.LANGUAGE] if mode else lg.profit_label_lang[self.LANGUAGE])
        # ax.set_xlabel(lg.hover_annotation_day_lang[self.LANGUAGE])

        # ax.set_xticks(range(n_bars), formatted_list.keys())
        # ax.xaxis.set_major_locator(tic.MaxNLocator(2))

        # if mode:
        #     if overall:
        #         ax.set_yticks(np.arange(0, (max_value // 100) * 100 + 200, 50))
        #     else:
        #         ax.set_yticks(np.arange(0, (max_value // 10) * 10 + 20, 5))
        # else:
        #     if overall:
        #         ax.set_yticks(np.arange(0, (max_value // 10000) * 10000 + 20000, 2500))
        #     else:
        #         ax.set_yticks(np.arange(0, (max_value // 1000) * 1000 + 2000, 500))

        fig.tight_layout()

        # cursor = mplcursors.cursor([rects1, rects2], hover='True')
        # @cursor.connect("add")
        # def on_add(sel):
        #     x, y, width, height = sel.artist[sel.index].get_bbox().bounds
        #     sel.annotation.set(text=f'{lg.hover_annotation_day_lang[self.LANGUAGE]}: {self.per_first[sel.index]}\n{lg.hover_annotation_value_lang[self.LANGUAGE]} {height}', position=(0, 20), anncoords="offset points")
        #     sel.annotation.xy = (x + width / 2, y + height)
        #     sel.annotation.get_bbox_patch().set(fc='#F2EDD7FF', alpha=0.6)
            
        # if mode:
        #     fig.savefig(f"graphs/purchases_{self.graph_period_start.strftime('%B %Y')}-{self.graph_period_end.strftime('%B %Y')}.png", bbox_inches='tight')
        # else:
        #     fig.savefig(f"graphs/profit_{self.graph_period_start.strftime('%B %Y')}-{self.graph_period_end.strftime('%B %Y')}.png", bbox_inches='tight')
        plt.show()
