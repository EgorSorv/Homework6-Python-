# Задача 30: Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# Решение:
# def arith_prog (a1, d, n):
#     array = []
#     for i in range(n):
#         array.append(a1 + i * d)
#     return array

# a1 = int(input('Введите первый элемент арифметической прогрессии: '))
# d = int(input('Введите разность между элементами прогрессии: '))
# n = int(input('Введите количество элементов: '))

# print(f'Арифметическая прогрессия => {", ".join(str(i) for i in arith_prog(a1, d, n))}')


# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# Решение:
# from random import randint

# def create_filled_array(length):
#     array = []
#     for _ in range(length):
#         array.append(randint(-100, 100))
#     return array

# def find_index(array1):
#     array2 = []
#     for i in range(len(array1)):
#         if min <= array1[i] <= max:
#             array2.append(i)
#     return array2

# length = int(input('Введите длину списка: '))
# min = int(input('Введите минимальное значение для поиска: '))
# max = int(input('Введите максимальное значение для поиска: '))

# array = create_filled_array(length)

# print()
# print('Полученный список:')
# print(array)

# print(f'Индексы элементов, находящихся в пределе [{min};{max}]:')
# print(", ".join(str(i) for i in find_index(array)))
