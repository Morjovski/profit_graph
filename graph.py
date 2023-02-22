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
        self.colors = [plt.cm.tab10(i) for i in range(12)]
        plt.rcParams["figure.autolayout"] = True

    def create_graph_bar(self, formatted_list, label, legend_name, interval, periods, mode):
        """Compare two periods by grouped bar chart style"""
        colors_list = []
        fig, ax = plt.subplots()
        fig.set_size_inches(20, 10)
        n_bars = len(formatted_list)
        total_width = 0.8
        bar_width = total_width / n_bars

        for i, values in enumerate(formatted_list):
            x_offset = (i - n_bars / 2) * bar_width + bar_width / 2
            if interval != 1:
                for x, y in enumerate(values):
                    ax.bar(x + x_offset, y, label=label[i], width=bar_width * 0.9, color=self.colors[i])
            else:
                ax.bar(i, values, label=label[i], width=bar_width * 0.9, color=self.colors[i])
            colors_list.append(self.colors[i])

        if mode:
            ax.set_title(f"{lg.purchases_title_lang[self.LANGUAGE]} {' '.join(periods)}")
            ax.set_ylabel(lg.purchases_label_lang[self.LANGUAGE])
        else:
            ax.set_title(f"{lg.profit_title_lang[self.LANGUAGE]} {' '.join(periods)}")
            ax.set_ylabel(lg.profit_label_lang[self.LANGUAGE])
        ax.set_xlabel(lg.hover_annotation_day_lang[self.LANGUAGE])

        plt.xticks(range(len(label)), label)

        leg = plt.legend(legend_name, loc='center left', bbox_to_anchor=(1, 0.5))

        for i, j in enumerate(leg.legendHandles):
            j.set_color(self.colors[i])

        fig.tight_layout()

        cursor = mplcursors.cursor()

        @cursor.connect("add")
        def on_add(sel):
            x, y, width, height = sel.artist[sel.index].get_bbox().bounds
            sel.annotation.set(text=f'\n{lg.hover_annotation_value_lang[self.LANGUAGE]} {height}\n')
            sel.annotation.xy = (x + width / 2, y + height / 2)
            sel.annotation.get_bbox_patch().set(fc='#F2EDD7FF', alpha=0.6)

        plt.subplots_adjust(right=0.7)

        plt.savefig(f"graphs/graph_{'_'.join(periods)}.png", bbox_inches='tight', dpi=300)

        plt.show()
