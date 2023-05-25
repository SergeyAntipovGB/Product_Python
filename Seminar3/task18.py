'''
Задача 18: Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой
строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка
содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
'''
from random import randint

n = int(input('введи количество элементов массива N = '))
a = [randint(0, 11) for i in range(n)]
print(a)
x = int(input('введи любое целое число X = '))
count = -100
for i in a:
	if x == i or (x > i and (count > x and count - x > x -
			  i or x > i > count)) or (x < i and (count < x and x - count > i - x or count > i > x)):
		count = i
print(f'самое близкое значение = {count}')