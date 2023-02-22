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

    def create_graph_bar(self, formatted_list, label, legend_name, interval, periods):
        """Compare two periods by grouped bar chart style"""
        
        fig, ax = plt.subplots()
        fig.set_size_inches(15, 10)
        colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
        n_bars = len(formatted_list)
        if n_bars < 3:
            total_width = 0.5
        else:
            total_width = 0.8
        bar_width = total_width / n_bars

        for i, values in enumerate(formatted_list):
            x_offset = (i - n_bars / 2) * bar_width + bar_width / 2
            if interval != 1:
                for x, y in enumerate(values):
                    ax.bar(x + x_offset, y, label=label[i], width=bar_width * 0.9, color=colors[i % len(colors)])
            else:
                ax.bar(i, values, label=label[i], width=bar_width * 0.9, color=colors[i % len(colors)])                


        # Update this
        ax.set_title(f"{lg.purchases_title_lang[self.LANGUAGE]} {self.graph_period_start.strftime('%B %Y')} - {self.graph_period_end.strftime('%B %Y')}"
                     if mode else f"{lg.profit_title_lang[self.LANGUAGE]} {self.graph_period_start.strftime('%B %Y')} - {self.graph_period_end.strftime('%B %Y')}")
        ax.set_ylabel(lg.purchases_label_lang[self.LANGUAGE] if mode else lg.profit_label_lang[self.LANGUAGE])
        ax.set_xlabel(lg.hover_annotation_day_lang[self.LANGUAGE])
        

        plt.xticks(range(len(label)), label)

        fig.tight_layout()
        print(f"{label}\n{legend_name}")

        cursor = mplcursors.cursor()
        @cursor.connect("add")
        def on_add(sel):
            x, y, width, height = sel.artist[sel.index].get_bbox().bounds
            sel.annotation.set(text=f'\n{lg.hover_annotation_value_lang[self.LANGUAGE]} {height}\n')
            sel.annotation.xy = (x + width / 2, y + height / 2)
            sel.annotation.get_bbox_patch().set(fc='#F2EDD7FF', alpha=0.6)
            
        fig.savefig(f"graphs/graph_{'_'.join(periods)}.png", bbox_inches='tight')
    
        plt.show()
