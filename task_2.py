# Задайте список из n чисел последовательности (1 + 1/n)^n, выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

n = int(input("\nВедите число n: "))
sumsum_elements = 0

def sequence(n):
    return [round((1 + 1 / i)**i, 2)
            for i in range(1, n + 1)]

for i in range(1, n + 1):
    sumsum_elements += ((1 + 1 / i) ** i)

print(f'\nДля n={n} -> {sequence(n)}')
print(f'Сумма: {sumsum_elements:.2f}')
