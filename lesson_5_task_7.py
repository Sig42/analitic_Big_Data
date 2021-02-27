import json
with open('task_7.json', 'w') as jf:
    with open('lesson_5_task_7.txt', 'r', encoding='utf-8') as d:
        dict_1 = {i.split()[0]: int(i.split()[2]) - int(i.split()[3]) for i in d}
        print(dict_1)
        sum_profit = 0
        for i in dict_1.values():
            if i > 0:
                sum_profit += int(i)
        print(sum_profit)
        average = round(sum_profit / len([i for i in dict_1.values() if i > 0]))
        print(average)
        result = [dict_1, {'average profit': average}]
        print(result)
    json.dump(result, jf)
