from add_data import AddData
from graph import Graph

class Mode():

    def __init__(self):
        self.ad = AddData(self)
        self.g = Graph(self)
        self.m = self.select()

    def select(self):
        n = input(f'Ввод прибыли (1)\nСмотреть график (2)): ')
        if n == '1':
            how_much = int(input('Дат много?: Да (1), Нет (0): '))
            if not how_much:
                self.ad.adding_data()
            else:
                self.ad.add_many_data()
        elif n == '2':
            per = input('Какой год\месяц? (YYYY или YYYY-MM): ')
            self.g.create_data(per)
            self.g.create_graph()
        else:
            print('Некорректный ввод данных!\n')
            Mode.select(self)

if __name__ == '__main__':
    gr = Mode()