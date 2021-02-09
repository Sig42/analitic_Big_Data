from functools import reduce
from itertools import count
from itertools import cycle
from math import factorial


# # Home work 1
# def salary(money, hours, premium):
#     result = money * hours + premium
#     return result
#
#
# print(salary(200, 8, 500))

# # # Home work 2
# original_list = [2, 45, 3, 87, 43, 3, 5, 75, 499, 5, 0, 5, 67]
# final_list = [original_list[i+1] for i in range(len(original_list)-1) if (original_list[i+1] - original_list[i]) > 0]
# print(final_list)

# Home work 3
# one_string = [i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0]
# print(one_string)

# Home work 4
# big_list = [3, 4, 3, 6, 6, 6, 55, 2, 1, 45, 2, 1, 67, 5, 4, 89, 6]
# result_list = [i for i in big_list if big_list.count(i) < 2]
# print(result_list)

# Home work 5
# great_list = [i for i in range(100, 1001, 2)]
#
#
# def my_func(p_1, p_2):
#     return p_1 * p_2
#
#
# result = reduce(my_func, great_list)
# print(result)

# Home work 6
# for i in count(15):
#     if i > 23:
#         break
#     else:
#         print(i)

# j = 0
# for k in cycle('BBKing'):
#     if j > 11:
#         break
#     print(k)
#     j += 1

# Home work 7
# def fact(n):
#     for i in range(n):
#         yield factorial(i + 1)
#
#
# for el in fact(5):
#     print(el)
