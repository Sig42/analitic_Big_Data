with open('task_4_to_write.txt', 'w', encoding='utf-8') as w:
    with open('task_4.txt', 'r', encoding='utf-8') as r:
        r_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
        empty = []
        for i in r:
            empty.append(i.replace(i.split()[0], r_dict.get(i.split()[0])))
        for i in empty:
            w.write(str(i))
