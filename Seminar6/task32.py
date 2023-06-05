'''
Задача 32:
Определить индексы элементов массива (списка), значения
которых принадлежат заданному диапазону (т.е. не меньше
заданного минимума и не больше заданного максимума)
'''


def fun(count = 0):
    if count == len(massive): return result
    if min <= massive[count] <= max: result.append(count)
    return fun(count + 1)

massive = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10,
           2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min = -1
max = 5
result = list()
print(fun())