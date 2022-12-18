# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
# максимум использование библиотеки Random для и получения случайного int

import random
from random import randint

n = int(input("\nВедите число n: "))

def initial_list(n):
    rand_list = []
    for i in range(n):
        rand_list.append(random.randint(1, 99))
    return rand_list

def mixed_list(first_list):
    my_randoms = []
    my_randoms = random.choices(first_list, k=len(first_list))
    return my_randoms

def random_number(second_list):
    ran_num = 0
    ran_num = random.choice(second_list)
    return ran_num

first_list = initial_list(n)
second_list = mixed_list(first_list)
num = random_number(second_list)
print(f'\nНачальный список {first_list}')
print(f'Перемешанный список:  {second_list}')
print(f'Получение случайного числа из перемешанного списка: {num}')
