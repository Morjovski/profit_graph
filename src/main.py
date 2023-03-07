import os
from time import sleep

from add_data import AddData
from graph import Graph
from create_data import CreateData
from random_data import RandomData
import language as lg


class Mode:

    def __init__(self):
        self.LANGUAGE = lg.choose_language()
        self.ad = AddData(self.LANGUAGE)
        self.cd = CreateData(self.LANGUAGE)
        self.g = Graph(self.LANGUAGE)
        self.random = RandomData(self.LANGUAGE)
        print(lg.select_language_lang[self.LANGUAGE])

    def select(self):
        """Main menu"""

        while True:
            print(lg.quit_program_lang[self.LANGUAGE])
            n = input(f'{lg.input_mode_lang[self.LANGUAGE]}')
            if n.lower() == 'random':
                self.random.randomize()
            elif n.lower() == 'quit':
                print(lg.exit_program_lang[self.LANGUAGE])
                sleep(1.5)
                quit()
            elif n == '1':
                self.ad.add_data()
            elif n == '2':
                if not os.path.exists(r'src/Database/entries.sqlite'):
                    print(lg.no_file_data_lang[self.LANGUAGE])
                    self.ad.add_data()
                else:
                    print(lg.back_main_menu_lang[self.LANGUAGE])
                    while True:
                        print(lg.interval_mode_lang[self.LANGUAGE])
                        interval = input(lg.interval_mode_input_lang[self.LANGUAGE])
                        if interval == 'q':
                            self.select()
                        try:
                            interval = int(interval)
                        except ValueError:
                            self._incorrect_data()
                            continue
                        if not 1 <= interval <= 3:
                            self._incorrect_data()
                            continue
                        break
                    while True:
                        mode = input(f'{lg.purchase_profit_mode_lang[self.LANGUAGE]}')
                        if mode == 'q':
                            self.select()
                        try:
                            mode = int(mode)
                        except ValueError:
                            self._incorrect_data()
                            continue
                        if not 1 <= mode <= 2:
                            self._incorrect_data()
                            continue
                        break
                    while True:
                        overall = input(lg.overall_mode_purchases_lang[self.LANGUAGE] if mode else lg.overall_mode_profit_lang[self.LANGUAGE])
                        if overall == 'q':
                            self.select()
                        try:
                            overall = int(overall)
                        except ValueError:
                            self._incorrect_data()
                            continue
                        if not 1 <= overall <= 2:
                            self._incorrect_data()
                            continue
                        break

                    periods = self.cd.take_period(interval)
                    format_data, label, legend_name, maxval, minval = self.cd.create_data(interval, overall, mode)
                    self.g.create_graph_bar(format_data, label, legend_name, interval, periods, mode, maxval, minval, overall)

            else:
                self._incorrect_data()
                continue

    def _incorrect_data(self):
        print(lg.incorrect_data_lang[self.LANGUAGE])
        sleep(1)


if __name__ == '__main__':
    gr = Mode()
    gr.select()
