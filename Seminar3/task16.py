'''
Задача 16: Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    3
    -> 1
'''
from random import randint

n = int(input('введи количество элементов массива N = '))
a = [randint(0, 11) for i in range(n)]
print(a)
x = int(input('введи любое Х число из массива > '))
count = 0
for i in a:
    if i == x:
        count += 1
print(f'заданное число встречается в массиве {count} раз')