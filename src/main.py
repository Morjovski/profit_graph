import os
from time import sleep

from add_data import AddData
from graph import Graph
from create_data import CreateData
from random_data import RandomData
import language as lg


LANGUAGE = 'EN'


class Mode:

    def __init__(self):
        self.LANGUAGE = lg.choose_language()
        self.ad = AddData(self.LANGUAGE)
        self.cd = CreateData(self.LANGUAGE)
        self.g = Graph(self.LANGUAGE)
        self.random = RandomData(self.LANGUAGE)

    def select(self):
        """Main menu"""

        print(lg.select_language_lang[self.LANGUAGE])
        while True:
            n = input(f'{lg.input_mode_lang[self.LANGUAGE]}')
            if n.lower() == 'random':
                self.random.randomize()
            elif n == '1':
                self.ad.add_data()
            elif n == '2':
                if not os.path.exists('Database\\entries.sqlite'):
                    print(lg.no_file_data_lang[self.LANGUAGE])
                    self.ad.add_data()
                else:
                    while True:
                        print(lg.interval_mode_lang[self.LANGUAGE])
                        try:
                            interval = int(input(lg.interval_mode_input_lang[self.LANGUAGE]))
                        except ValueError:
                            self.incorrect_data()
                            continue
                        if not 1 <= interval <= 3:
                            self.incorrect_data()
                            continue
                        break
                    while True:
                        try:
                            mode = int(input(f'{lg.purchase_profit_mode_lang[self.LANGUAGE]}'))
                        except ValueError:
                            self.incorrect_data()
                            continue
                        if not 1 <= mode <= 2:
                            self.incorrect_data()
                            continue
                        break
                    while True:
                        try:
                            overall = int(input(lg.overall_mode_purchases_lang[self.LANGUAGE] if mode else lg.overall_mode_profit_lang[self.LANGUAGE]))
                        except ValueError:
                            self.incorrect_data()
                            continue
                        if not 1 <= overall <= 2:
                            self.incorrect_data()
                            continue
                        break

                    periods = self.cd.take_period(interval)
                    formatted_list, label, legend_name, maxval, minval = self.cd.create_data(interval, overall, mode)
                    self.g.create_graph_bar(formatted_list, label, legend_name, interval, periods, mode, maxval, minval)

            else:
                self.incorrect_data()
                continue

    def incorrect_data(self):
        print(lg.incorrect_data_lang[self.LANGUAGE])
        sleep(1)


if __name__ == '__main__':
    gr = Mode()
    gr.select()
