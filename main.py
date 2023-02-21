import os

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
        self.random = RandomData()

    def select(self):
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
                        print('Просмотр графика за:')
                        print('За год в общем - (1)')
                        print('За год помесячно - (2)')
                        print('За месяц по дням - (3)')
                        interval = int(input("Выберите режим: "))
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

                    self.cd.take_period(interval)
                    formatted_list = self.cd.create_data(interval, overall, mode)
                    self.g.create_graph_bar(formatted_list)

            else:
                print(f'{lg.incorrect_data_lang[self.LANGUAGE]}\n')

    def incorrect_data(self):
        print(lg.incorrect_data_lang[self.LANGUAGE])


if __name__ == '__main__':
    gr = Mode()
    gr.select()
