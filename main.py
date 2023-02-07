import os

from add_data import AddData
from graph import Graph
from create_data import CreateData
from random_data import RandomData


class Mode:

    def __init__(self):
        self.ad = AddData()
        self.cd = CreateData()
        self.g = Graph()
        self.random = RandomData()

    def select(self):
        n = input(f'Ввод прибыли (1)\nСмотреть график (2)): ')
        if n == '1':
            self.ad.add_data()
        elif n == '2':
            if not os.path.exists('data.json'):
                print("There is no 'data.json' file! Enter the data below:")
                self.ad.add_data()
            else:
                while True:
                    try:
                        mode = int(input('Просмотр прибыли (0), просмотр кол-ва продаж (1): '))
                        compare = int(input('Сравнить два периода? Да - (1), Нет (0): '))
                        overall = int(
                            input('Общее количество продаж за период? (Да (1), Нет(0)): ' if mode else 'Общая прибыль за период? (Да (1), Нет(0)): ')
                        )
                        break
                    except ValueError:
                        print('Некорректный ввод данных!')
                    except SyntaxError:
                        print('Некорректный ввод данных!')
                    except TypeError:
                        print('Некорректный ввод данных!')

                if compare:
                    per_start = input('Введите начало периода (YYYY-MM): ')
                    per_end = input('Введите конец периода (YYYY-MM): ')
                    self.g.take_period(per_start, per_end)
                else:
                    per = input('Какой год\месяц? (YYYY-MM): ')
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
            print('Некорректный ввод данных!\n')
            gr.select()


if __name__ == '__main__':
    gr = Mode()
    gr.select()
