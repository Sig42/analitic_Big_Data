# Home work 1
def div(n_1, n_2):
    try:
        result = n_1 / n_2
        print(result)
    except:
        print('На ноль делить нельзя')


div(10, 0)

# Home work 2
# def blanket(name, surname, born, city, email, phone):
#     dict = {
#         'name': name,
#         'surname': surname,
#         'year of born': born,
#         'city of born': city,
#         'email': email,
#         'phone number': phone
#     }
#     print(dict)
#
#
# blanket('hy', 'fg', 1988, 'aba', 'df', 8765)

# Home work 3
# def maxi_max(n_1, n_2, n_3):
#     m = max(n_1, n_2, n_3)
#     numbers = [n_1, n_2, n_3]
#     numbers.remove(m)
#     mm = max(numbers)
#     print(m + mm)
#
#
# maxi_max(1, 2, 500)

# Home work 4
# def my_func(x, y):
#     u = abs(y)
#     what = x ** u
#     print(what)
#     z = x
#     while u >= 2:
#         u -= 1
#         x = x * z
#     print(x)
#
#
# my_func(4, 6)

# Home work 5
# def my_sum():
#     finish = 0
#     while True:
#         begin_list = input('Введите какое-то количество чисел (если надоело нажмите - x): ')
#         if begin_list == 'x':
#             print('Ну не хочешь как хочешь...')
#             break
#         split_list = begin_list.split(' ')
#         empty = []
#         for i in range(len(split_list)):
#             a = int(split_list[i])
#             empty.append(a)
#
#         result = sum(empty)
#         finish = finish + result
#         print(finish)
#
#
# my_sum()

# Home work 6
# def int_func(word):
#     result = word.title()
#     return result
#
#
# print(int_func('doom'))


# Home work 7
# def titles(words):
#     split_l = words.split(' ')
#     new_l = []
#     for i in split_l:
#         def int_func(word):
#             result = word.title()
#             return result
#
#         int_func(i)
#         a = int_func(i)
#         new_l.append(a)
#     print(' '.join(new_l))
#
#
# titles('i love it')
