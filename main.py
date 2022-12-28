from add_data import AddData

class Mode():

    def __init__(self):
        self.ad = AddData(self)
        self.m = self.select()

    def select(self):
        n = input(f'Ввод прибыли (1)\nСмотреть график (2))\nВыберите режим: ')
        if n == '1':
            self.ad.adding()
        elif n == '2':
            print('Просмотр графика')
        else:
            print('Некорректный ввод данных!\n')
            Mode.select(self)

if __name__ == '__main__':
    gr = Mode()