# Домашнее задание № 1
# a = 10
# b = a + 12
# c = 'Hello World'
# d = int(input('Введите трехзначное число: '))
# e = str(input('Введите Ваше имя: '))
# print(a, b, c, d, e)

# Домашнее задание № 2
# number = int(input('Введите четырехзначное число: '))
# not_minutes = number // 60
# seconds = number - (not_minutes * 60)
# hours = not_minutes // 60
# minutes = not_minutes - (hours * 60)
# print('{:02}:{:02}:{:02}'.format(hours, minutes, seconds))

# Домашнее задание № 3
numb = int(input('Введите число: '))
numb_str = str(numb)
numb_nn = int(numb_str + numb_str)
numb_nnn = int(numb_str + numb_str + numb_str)
result = numb + numb_nn + numb_nnn
print(result)

# Домашнее задание № 4
# while True:
#     big_numb = int(input('Введите целое положительное число: '))
#     if 0 <= big_numb < 100:
#         res1 = big_numb // 10
#         res2 = big_numb % 10
#         if res1 > res2:
#             print(f'Наибольшая цифра в числе - {res1}')
#             break
#         else:
#             print(f'Наибольшая цифра в числе - {res2}')
#             print('Мы закончим, когда наибольшая цифра будет первой')
#     elif big_numb >= 100:
#         print('Нужно двузначное число')

# Домашнее задание № 5
# proceed = int(input('Введите сумму выручки: '))
# cost = int(input('Введите сумму расходов: '))
# results = proceed - cost
# if results > 0:
#     print(f'Ваш доход составил: {results} бубликов. Поздравляю!')
#     profitability = results / proceed
#     print(f'Рентабельность Вашей организации: {profitability} ёршиков.')
#     units = int(input('Сколько человек (функциональных биологических единиц) трудится в Вашей организации?: '))
#     results_per_unit = results / units
#     print(f'Вот столько получит каждый человек (биологическая функциональная единица),\nесли распределить прибыль '
#           f'между ними: {results_per_unit} каких-то единиц.')
# else:
#     print(f'Вы так себе предприниматель. Ваш финансовый результат: {results} бубликов.')

# # Домашнее задание № 6
# start = int(input('Сколько сегодня пробежали?: '))
# finish = int(input('А сколько бы хотели пробежать?: '))
# count = 0
# while start < finish:
#     count = count + 1
#     percent = start / 10
#     start = round(start + percent, 2)
#     print(f'{count}-й день: {start} км.')
# print(f'Поздравляю! И всего-то на {count}-й день!')
