import os

from add_data import AddData
from graph import Graph
from create_data import CreateData
from random_data import RandomData

import language as lg


LANGUAGE = 'EN'

class Mode:

    def __init__(self, LANGUAGE):
        self.LANGUAGE = LANGUAGE
        self.ad = AddData(self.LANGUAGE)
        self.cd = CreateData(self.LANGUAGE)
        self.g = Graph(self.LANGUAGE)
        self.random = RandomData()

    def select(self):
        n = input(f'{lg.input_mode_lang[self.LANGUAGE]}')
        if n == '1':
            self.ad.add_data()
        elif n == '2':
            if not os.path.exists('data.json'):
                print(lg.no_file_data_lang[self.LANGUAGE])
                self.ad.add_data()
            else:
                while True:
                    try:
                        mode = int(input(f'{lg.purchase_profit_mode_lang[self.LANGUAGE]}'))
                        if mode > 1:
                            raise ValueError
                        compare = int(input(f'{lg.compare_mode_lang[self.LANGUAGE]}'))
                        if compare > 1:
                            raise ValueError
                        overall = int(
                            input(lg.overall_mode_purchases_lang[self.LANGUAGE] if mode else lg.overall_mode_profit_lang[self.LANGUAGE])
                        )
                        if overall > 1:
                            raise ValueError
                        break
                    except ValueError:
                        print(lg.incorrect_data_lang[self.LANGUAGE])

                if compare:
                    per_start = input(f'{lg.per_start_lang[self.LANGUAGE]}')
                    per_end = input(f'{lg.per_end_lang[self.LANGUAGE]}')
                    self.g.take_period(per_start, per_end)
                else:
                    per = input(f'{lg.one_per_lang[self.LANGUAGE]}')
                    self.g.take_period(per)

                self.g.create_data(overall, mode)

                if mode:
                    if compare:
                        self.g.create_graph_bar(mode, overall)
                    elif overall:
                        self.g.create_graph(self.g.overall_list_start)
                    else:
                        self.g.create_graph(self.g.purchases_start)
                else:
                    if compare:
                        self.g.create_graph_bar(mode, overall)
                    elif overall:
                        self.g.create_graph(self.g.overall_list_start)
                    else:
                        self.g.create_graph(self.g.profit_start)
        else:
            print(f'{lg.incorrect_data_lang[self.LANGUAGE]}\n')
            gr.select()


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
