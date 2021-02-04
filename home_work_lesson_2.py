# Home work 1
my_list = [1, 'one', [2, 'two'], 2.2, (1, 2, 3), {'horror'}, {'name': 'kik', 'age': 45}, True, b'some', None]
print(type(my_list[0]))
print(type(my_list[1]))
print(type(my_list[2]))
print(type(my_list[3]))
print(type(my_list[4]))
print(type(my_list[5]))
print(type(my_list[6]))
print(type(my_list[7]))
print(type(my_list[8]))
print(type(my_list[9]))

# Home work 2
# i_input = input('Введите предложение из какого-то количества слов: ')
# l_list = i_input.split()
# for i in range(len(l_list)):
#     if i % 2 == 0:
#         l_list.insert(i + 1, l_list.pop(i))
#         print(l_list)

# Home work 3
# user = int(input('Введите месяц в виде цифры (1 - январь, 12 - декабрь...: '))
# months = {'1': 'январь',
#           '2': 'февраль',
#           '3': 'март',
#           '4': 'апрель',
#           '5': 'май',
#           '6': 'июнь',
#           '7': 'июль',
#           '8': 'август',
#           '9': 'сентябрь',
#           '10': 'октябрь',
#           '11': 'ноябрь',
#           '12': 'декабрь'
#           }
# seasons = ['winter', 'spring', 'summer', 'autumn']
# if user == 12 or user < 3:
#     print(seasons[0])
# elif 2 < user <= 5:
#     print(seasons[1])
# elif 5 < user <= 8:
#     print(seasons[2])
# elif 8 < user <= 11:
#     print(seasons[3])
# else:
#     print('Что тут не так...')

# Home work 4
# hello = input('Привет! Как сам? Не стесняйся, напиши побольше слов: ')
# h_list = hello.split()
# for i, e in enumerate(h_list, 1):
#     print(i, e[0:10])

# Home work 5
# numbers = [7, 5, 3, 3, 2]
# get_in = int(input('Введите какое-нибудь натуральное число: '))
# numbers.append(get_in)
# numbers.sort()
# numbers.reverse()
# print(numbers)
