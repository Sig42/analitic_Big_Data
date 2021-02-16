with open('task_6.txt', 'r', encoding='utf-8') as d:
    b_dict = {}
    for i in d:
        name, vol = i.split(':')
        b_sum = sum(map(int, ''.join([i for i in vol if i == ' ' or ('0' <= i <= '9')]).split()))
        b_dict[name] = b_sum
    print(b_dict)
