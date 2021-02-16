with open('lesson5.txt', 'w', encoding='utf-8') as j:
    while True:
        x = input('Введите строку (если хватит введите - stop): ')
        j.write(x+'\n')
        if x == 'stop':
            break
print('end')
