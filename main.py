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
                            self.incorrect_data(self)
                            continue
                        break
                    while True:
                        mode = int(input(f'{lg.purchase_profit_mode_lang[self.LANGUAGE]}'))
                        if mode > 1:
                            self.incorrect_data(self)
                            continue
                        break
                    while True:
                        compare = int(input(f'{lg.compare_mode_lang[self.LANGUAGE]}'))
                        if compare > 1:
                            self.incorrect_data(self)
                            continue
                        break
                    while True:
                        overall = int(
                            input(lg.overall_mode_purchases_lang[self.LANGUAGE] if mode else lg.overall_mode_profit_lang[self.LANGUAGE])
                        )
                        if overall > 1:
                            self.incorrect_data(self)
                            continue
                        break

                    # Можно отделить в отдельный метод (Или переместить в метод take_period файла create_data )
                    periods = []
                    if interval == 1:
                        periods.append(input('Введите года через запятую (Формат YYYY): ').split())
                    elif interval == 2:
                        periods.append(input('Введите год в формате "yyyy": ').split())
                    else:
                        periods.append(input('Введите год и месяц в формате "yyyy-mm": ').split())

                    self.g.take_period(interval, periods)  
                    # if compare:
                    #     periods = []
                    #     if interval == 3:
                    #         for _ in range():
                    #             periods.append(input(f'{lg.per_start_lang[self.LANGUAGE]}'))
                    #     else:
                    #         for _ in range():
                    #             periods.append(input(f'{lg.per_start_lang[self.LANGUAGE]}'))
                    #     self.g.take_period(periods)
                    # else:
                    #     periods = []
                    #     if interval == 3:
                    #         periods = input(f'{lg.one_per_lang[self.LANGUAGE]}').split()
                    #     else:
                    #         periods.append(input(f'{lg.one_per_lang[self.LANGUAGE]}'))
                    #     self.g.take_period(periods)
                    self.g.create_data(interval, overall, mode)
                    self.nonamefun(self, interval, mode, compare, overall)
            else:
                print(f'{lg.incorrect_data_lang[self.LANGUAGE]}\n')

    def nonamefun(self, interval, mode, compare, overall):
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

    def incorrect_data(self):
        print(lg.incorrect_data_lang[self.LANGUAGE])

if __name__ == '__main__':
    gr = Mode()
    gr.select()
