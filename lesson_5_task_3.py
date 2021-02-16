with open('task_3.txt', 'r') as j:
    empty = []
    for i in j:
        empty.append(i.split())
    print(empty)
    a = 0
    for i in empty:
        a = a + int(i[1])
        if int(i[1]) < 20000:
            print(f'Оклад меньше 20000 у следующих сотрудников: {i[0]}')
    r = a / len(empty)
    print(f'Средняя сумма оклада: {r}')
