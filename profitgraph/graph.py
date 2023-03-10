import matplotlib.pyplot as plt
import mplcursors
import os

from .create_data import CreateData
from . import language as lg


class Graph(CreateData):

    def __init__(self, LANGUAGE):
        self.LANGUAGE = LANGUAGE
        super().__init__(LANGUAGE)
        self.colors = [plt.cm.tab10(i) for i in range(12)]
        plt.style.use('_mpl-gallery')
        plt.rcParams["figure.autolayout"] = True
        self.dir_path = os.path.dirname(__file__)


    def create_graph_bar(self, format_data, label, legend_name, interval, periods, mode, maxval, minval, overall):
        """Compare two periods by grouped bar chart style"""
        
        fig, ax = plt.subplots()
        fig.set_size_inches(20, 10)
        n_bars = len(format_data)
        total_width = 0.8
        bar_width = total_width / n_bars

        for i, values in enumerate(format_data):
            x_offset = (i - n_bars / 2) * bar_width + bar_width / 2
            if interval != 1:
                for x, y in enumerate(values):
                    ax.bar(x + x_offset, y, label=label[x], width=bar_width * 0.9, color=self.colors[i])
                    if overall == 2:
                        if y == maxval:
                            legend_max_color = self.colors[i]
                        if y == minval:
                            legend_min_color = self.colors[i]
            else:
                ax.bar(i, values, label=label[i], width=bar_width * 0.9, color=self.colors[i])
                if overall == 2:
                    if values[0] == maxval:
                        legend_max_color = self.colors[i]
                    if values[0] == minval:
                        legend_min_color = self.colors[i]

        # For add min/max legend
        if interval == 1:
            for i in range(2):
                plt.bar(i, 0, color='none')

        if mode == 2:
            ax.set_title(f"{lg.purchases_title_lang[self.LANGUAGE]} {', '.join(periods)}")
            ax.set_ylabel(lg.purchases_label_lang[self.LANGUAGE])
        else:
            ax.set_title(f"{lg.profit_title_lang[self.LANGUAGE]} {', '.join(periods)}")
            ax.set_ylabel(lg.profit_label_lang[self.LANGUAGE])
        ax.set_xlabel(lg.hover_annotation_day_lang[self.LANGUAGE])

        plt.xticks(range(len(label)), label)

        leg = plt.legend(legend_name, loc='center left', bbox_to_anchor=(1, 0.5))

        # Create a legend color
        for i, j in enumerate(leg.legendHandles):
            j.set_color(self.colors[i])

        # To set min max color exactly the same as min max period
        if overall == 2:
            leg.legendHandles[-2].set_color(legend_max_color)
            leg.legendHandles[-1].set_color(legend_min_color)

        fig.tight_layout()

        if interval == 1:
            date = lg.hover_annotation_year_lang[self.LANGUAGE]
        elif interval == 2:
            date = lg.hover_annotation_month_lang[self.LANGUAGE]
        else:
            date = lg.hover_annotation_day_lang[self.LANGUAGE]

        # Hover to show bar values
        cursor = mplcursors.cursor()

        @cursor.connect("add")
        def on_add(sel):
            x, y, width, height = sel.artist[sel.index].get_bbox().bounds
            sel.annotation.set(text=f'\n{date} {sel.artist.get_label()}\n{lg.hover_annotation_value_lang[self.LANGUAGE]} {height}\n')
            sel.annotation.xy = (x + width / 2, y + height)
            sel.annotation.get_bbox_patch().set(fc='#F2EDD7FF', alpha=0.8)

        plt.subplots_adjust(right=0.7)

        if mode == 2:
            folder_name = self.dir_path + "\\graphs\\purchases"
            os.makedirs(folder_name, exist_ok=True)
            purchase_file = self.dir_path + f"graphs\\purchases\\purchases_graph_{'_'.join(periods)}.png"
            plt.savefig(purchase_file, bbox_inches='tight', dpi=300)
            print(f"'purchases_graph_{'_'.join(periods)}.png' {lg.purchases_img_save_lang[self.LANGUAGE]} {folder_name}")
        else:
            folder_name = self.dir_path + "\\graphs\\profit"
            os.makedirs(folder_name, exist_ok=True)
            profit_file = self.dir_path + f"\\graphs\\profit\\profit_graph_{'_'.join(periods)}.png"
            plt.savefig(profit_file, bbox_inches='tight', dpi=300)
            print(f"'profit_graph_{'_'.join(periods)}.png' {lg.profit_img_save_lang[self.LANGUAGE]} {folder_name}")

        plt.show()
