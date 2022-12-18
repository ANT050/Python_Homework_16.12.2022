# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

num = input('\nВведите число: ')

def summa(num):
    if float(num) < 0:
        num = float(num) * (-1)
    sum_number = 0

    for i in str(num):
        if i != '.':
            sum_number += int(i)
    return sum_number

print(f'{num} -> {summa(num)}')
