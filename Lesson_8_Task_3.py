class MyExcept:
    def __init__(self, param):
        self.list_l = [param]
        while True:
            try:
                a = int(input('Введите число: '))
                self.list_l.append(a)
            except ValueError:
                print('Ввод данных некорректен. Введите ЧИСЛО.')
            else:
                print(f'Ввод данных корректен. Результат {self.list_l}')
            finally:
                final = input('Если хотите продолжить - жмите enter\nЕсли хотите завершить - жмите s')
                if final == 's':
                    print(f'Процесс завершен. Результат: {self.list_l}')
                    break


obj = MyExcept(0)
