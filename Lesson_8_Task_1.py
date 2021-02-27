class Data:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def get_data(cls, day, month, year):
        cls.day = int(day)
        cls.month = int(month)
        cls.year = int(year)
        return f'{cls.day} {cls.month} {cls.year}'

    @staticmethod
    def valid(day, month, year):
        if 31 < day < 1:
            print('Неверное значение day!')
        elif 12 < month < 1:
            print('Неврное значение month!')
        elif year > 2021:
            print('Неверное значение year!')
        else:
            print('Значения введены верно!')


print(Data.get_data('1', '12', '2010'))
Data.valid(12, 10, 2020)
