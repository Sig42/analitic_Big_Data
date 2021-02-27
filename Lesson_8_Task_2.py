class ExceptionZero:
    def __init__(self, n_1, n_2):
        self.n_1 = n_1
        self.n_2 = n_2

    @property
    def division(self):
        try:
            return round(self.n_1 / self.n_2, 2)
        except ZeroDivisionError:
            return 'Деление на ноль невозможно!'


a = ExceptionZero(int(input('Введите что будем делить: ')), int(input('Введите на что будем делить: ')))
print(a.division)
