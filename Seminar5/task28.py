'''
Задача 28: Вводится десятичное число. Реализовать алгоритм его
перевода в двоичную систему счисления через рекурсию. Нельзя
использовать функцию bin()

*Пример:*
    10
    *Вывод:*
    1010
'''


def bynar(num):
    if num == 0: return '0'
    elif num == 1: return '1'
    return f'{bynar(num // 2)}{num % 2}'

dec = int(input('целое десятичное число > '))
print(f'двоичное значение = {bynar(dec)}')