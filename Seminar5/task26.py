'''
Задача 26:  Напишите программу, которая на вход принимает два числа
A и B, и возводит число А в целую степень B с помощью рекурсии.

*Пример:*
A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 
'''


def recurse(base, degree):
    if degree == 0: return 1
    base *= recurse(base, degree - 1)
    return base
    
a = int(input('введи основание степени А = '))
b = int(input('введи показатель степени В = '))
print(f'A = {a}; B = {b} -> {recurse(a, b)}')