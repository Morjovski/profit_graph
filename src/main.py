import os

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

        while True:
            n = input(f'{lg.input_mode_lang[self.LANGUAGE]}')
            if n.lower() == 'random':
                self.random.randomize()
            elif n == '1':
                self.ad.add_data()
            elif n == '2':
                if not os.path.exists('entries.sqlite'):
                    print(lg.no_file_data_lang[self.LANGUAGE])
                    self.ad.add_data()
                else:
                    while True:
                        print(lg.interval_mode_lang[self.LANGUAGE])
                        interval = int(input(lg.interval_mode_input_lang[self.LANGUAGE]))
                        if interval < 1 or interval > 3:
                            self.incorrect_data()
                            continue
                        break
                    while True:
                        mode = int(input(f'{lg.purchase_profit_mode_lang[self.LANGUAGE]}'))
                        if mode > 1:
                            self.incorrect_data()
                            continue
                        break
                    while True:
                        overall = int(
                            input(lg.overall_mode_purchases_lang[self.LANGUAGE] if mode else lg.overall_mode_profit_lang[self.LANGUAGE])
                        )
                        if overall > 1:
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


if __name__ == '__main__':
    
    while True:
        LANGUAGE = input('Choose a language\nВыберите язык\nОберіть мову\nEN/RU/UA: ')
        if len(LANGUAGE) == 0 or LANGUAGE.lower() == 'en':
            LANGUAGE = 'EN'
            break
        elif LANGUAGE.lower() == 'ru':
            LANGUAGE = 'RU'
            break
        elif LANGUAGE.lower() == 'ua':
            LANGUAGE = 'UA'
            break
        else:
            print('Incorrect lang select!\nВведены неправилные данные!\nВведено неправильні дані!')
            continue

    gr = Mode(LANGUAGE)
    gr.select()
