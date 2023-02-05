from add_data import AddData
from graph import Graph
from create_data import CreateData
from average import Average
from random_data import RandomData


class Mode:

    def __init__(self):
        self.ad = AddData()
        self.cd = CreateData()
        self.g = Graph()
        self.avg = Average()
        self.random = RandomData()

    def select(self):
        n = input(f'Ввод прибыли (1)\nСмотреть график (2)): ')

        if n == '1':
            random = input('Для создания случайных значений, введите "random": ')
            if random.lower() == 'random':
                self.random.randomize()
            else:
                self.ad.add_data()
        elif n == '2':
            mode = int(input('Просмотр прибыли (0), просмотр кол-ва продаж (1): '))
            compare = int(input('Сравнить два периода? Да - (1), Нет (0): '))
            overall = int(
                input(
                'Общее количество продаж за период? (Да (1), Нет(0)): ' 
                if mode else 
                'Общая прибыль за период? (Да (1), Нет(0)): '
                )
            )

            if compare:
                per_start = input('Введите начало периода (YYYY-MM): ')
                per_end = input('Введите конец периода (YYYY-MM): ')
                self.g.take_period(per_start, per_end)
            else:
                self.per = input('Какой год\месяц? (YYYY-MM): ')
                self.g.take_period(self.per)

            self.g.create_data(overall, mode)

            if mode:
                if compare:
                    self.g.create_graph_bar(mode, overall)
                else:
                    self.g.create_graph(self.g.purchases_start)
            else:
                if compare:
                    self.g.create_graph_bar(mode, overall)
                else:
                    self.g.create_graph(self.g.profit_start)
        else:
            print('Некорректный ввод данных!\n')
            gr.select()

if __name__ == '__main__':
    gr = Mode()
    gr.select()
