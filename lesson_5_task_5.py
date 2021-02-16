with open('task_5.txt', 'w+', encoding='utf-8') as f:
    input_l = input('Введите произвольное количество чисел через пробел: ')
    f.write(input_l)
    split_l = input_l.split(' ')
    sum_of = 0
    for i in split_l:
        sum_of += int(i)
    print(sum_of)
