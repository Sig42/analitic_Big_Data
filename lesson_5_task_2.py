with open('task_2.txt', 'r') as j:
    empty = []
    for i in j:
        empty.append(i)
    print(f'Количество строк в файле {len(empty)}')
    for i in range(len(empty)):
        print(f'В строке {i+1} символов - {len(empty[i])}')
