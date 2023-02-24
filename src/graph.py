import matplotlib.pyplot as plt
import mplcursors
import os

from create_data import CreateData
import language as lg


class Graph(CreateData):

    def __init__(self, LANGUAGE):
        self.LANGUAGE = LANGUAGE
        super().__init__(LANGUAGE)
        plt.style.use('_mpl-gallery')
        self.colors = [plt.cm.tab10(i) for i in range(12)]
        plt.rcParams["figure.autolayout"] = True

    def create_graph_bar(self, formatted_list, label, legend_name, interval, periods, mode, maxval, minval):
        """Compare two periods by grouped bar chart style"""
        
        fig, ax = plt.subplots()
        fig.set_size_inches(20, 10)
        n_bars = len(formatted_list)
        total_width = 0.8
        bar_width = total_width / n_bars

        for i, values in enumerate(formatted_list):
            x_offset = (i - n_bars / 2) * bar_width + bar_width / 2
            if interval != 1:
                for x, y in enumerate(values):
                    ax.bar(x + x_offset, y, label=label[x], width=bar_width * 0.9, color=self.colors[i])
                    if y == maxval:
                        legend_max_color = self.colors[i]
                    if y == minval:
                        legend_min_color = self.colors[i]
            else:
                ax.bar(i, values, label=label[i], width=bar_width * 0.9, color=self.colors[i])
                if values[0] == maxval:
                    legend_max_color = self.colors[i]
                if values[0] == minval:
                    legend_min_color = self.colors[i]

        # For add min/max legend
        if interval == 1:
            for i in range(2):
                plt.bar(i, 0, color='none')

        if mode:
            ax.set_title(f"{lg.purchases_title_lang[self.LANGUAGE]} {' '.join(periods)}")
            ax.set_ylabel(lg.purchases_label_lang[self.LANGUAGE])
        else:
            ax.set_title(f"{lg.profit_title_lang[self.LANGUAGE]} {' '.join(periods)}")
            ax.set_ylabel(lg.profit_label_lang[self.LANGUAGE])
        ax.set_xlabel(lg.hover_annotation_day_lang[self.LANGUAGE])

        plt.xticks(range(len(label)), label)

        leg = plt.legend(legend_name, loc='center left', bbox_to_anchor=(1, 0.5))

        # Create a legend color
        for i, j in enumerate(leg.legendHandles):
            j.set_color(self.colors[i])
        # To set min max color exactly the same as min max period
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

        os.makedirs('graphs/profit', exist_ok=True)
        os.makedirs('graphs/purchases', exist_ok=True)
        if mode:
            plt.savefig(f"graphs/purchases/purchases_graph_{'_'.join(periods)}.png", bbox_inches='tight', dpi=300)
        else:
            plt.savefig(f"graphs/profit/profit_graph_{'_'.join(periods)}.png", bbox_inches='tight', dpi=300)

        plt.show()
