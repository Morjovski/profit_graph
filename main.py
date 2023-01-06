from add_data import AddData
from graph import Graph

class Mode():

    def __init__(self):
        self.ad = AddData()
        self.g = Graph()
        self.m = self.select()

    def select(self):
        n = input(f'Ввод прибыли (1)\nСмотреть график (2)): ')
        if n == '1':
            how_much = int(input('Дата одна?: Нет (1), Да (0): '))
            if not how_much:
                self.ad.add_one_data()
            else:
                self.ad.add_many_data()
        elif n == '2':
            self.mode = int(input('Просмотр прибыли (0), просмотр кол-ва продаж (1): '))
            self.compare = int(input('Сравнить два периода? Да - (0), Нет (1):'))
            if not self.compare:
                self.per_start = input('Введите начало периода (YYYY или YYYY-MM): ')
                self.per_end = input('Введите конец периода (YYYY или YYYY-MM): ')
                self.g.take_period(self.per_start, self.per_end)
            else:
                self.per = input('Какой год\месяц? (YYYY или YYYY-MM): ')                
                self.g.take_period(self.per)
                self.g.create_data(self.per)
            if self.mode == 0:
                if self.compare == 1:
                    self.g.create_graph(self.g.profit)
                else:
                    self.g.create_graph_bar()
            elif self.mode == 1:
                self.g.create_graph(self.g.purchases)
        else:
            print('Некорректный ввод данных!\n')
            Mode.select(self)

if __name__ == '__main__':
    gr = Mode()