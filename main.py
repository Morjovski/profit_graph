from add_data import AddData
from graph import Graph
from create_data import CreateData
from average import Average


class Mode:

    def __init__(self):
        self.ad = AddData()
        self.cd = CreateData()
        self.g = Graph()
        self.avg = Average()

    def select(self):
        n = input(f'Ввод прибыли (1)\nСмотреть график (2)): ')
        if n == '1':
            how_much = int(input('Дата одна?: Нет (1), Да (0): '))
            if not how_much:
                self.ad.add_one_data()
            else:
                self.ad.add_many_data()
        elif n == '2':
            mode = int(input('Просмотр прибыли (0), просмотр кол-ва продаж (1): '))
            compare = int(input('Сравнить два периода? Да - (1), Нет (0): '))
            overall = int(input(
                'Общее количество продаж за период? (Да (1), Нет(0)): ' if mode else 'Общая прибыль за период? (Да (1), Нет(0)): '))
            if compare:
                self.per_start = input('Введите начало периода (YYYY или YYYY-MM): ')
                self.per_end = input('Введите конец периода (YYYY или YYYY-MM): ')
                self.g.take_period(self.per_start, self.per_end)
            else:
                self.per = input('Какой год\месяц? (YYYY или YYYY-MM): ')
                self.g.take_period(self.per)
                self.g.create_data(self.per, overall, mode)
            if mode:
                if compare:
                    self.g.create_graph_bar(mode, overall)
                else:
                    self.g.create_graph(self.g.purchases)
            else:
                if compare:
                    self.g.create_graph_bar(mode, overall)
                else:
                    self.g.create_graph(self.g.profit)

        else:
            print('Некорректный ввод данных!\n')
            Mode.select(self)

if __name__ == '__main__':
    gr = Mode()
    gr.select()