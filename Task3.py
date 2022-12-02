# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18 [4.07, 5.1, 8.2444, 6.9814] - 0.9114 или 9114

import random
import math
def fill_list(in_list: list, n: int) -> list:
    '''
    Возвращает список, заполненный случайными числами.

        Args:
            in_list (list) - пустой список
            n (int) - число, которое задаёт пользователь, которое определяет размер списка  
        Returns:
            in_list (list) - список, заполненный случайными вещественными числами
    '''
    for i in range(0, n):
        in_list.append(round((random.randint(0, 10) + random.random()), 5))
    print(f'Исходный список: {in_list}')

def form_fraction_list(in_list: list, n_list: list, n: int) -> list:
    '''
    Возвращает список, заполненный дробной частью элементов исходного списка.

        Args:
            in_list (list) - список, заполненный случайными вещественными числами
            n_list (list) - пустой список
            n (int) - число, которое задаёт пользователь, которое определяет размер списка  
        Returns:
            n_list (list) - список, заполненный дробной частью элементов исходного списка
    '''
    for i in range(0, n):
        n_list.append(round((in_list[i] - math.floor(in_list[i])), 5))
    print(f'Дробный список:  {n_list}')

def compare_min_max(n_list: list) -> float:
    '''
    Возвращает число - разницу между макс. и мин. значением дробной части элементов

        Args:
            n_list (list) - список, заполненный дробной частью элементов исходного списка
        Returns:
            diff (int) - число - разница между макс. и мин. значением дробной части элементов
    '''
    diff = round((max(n_list) - min(n_list)), 5)
    print(f'Разница:  {diff}')

size = abs(int(input('Количество элементов в списке: ')))
init_list = []
fraction_list = []

fill_list(init_list, size)
form_fraction_list(init_list, fraction_list, size)
compare_min_max(fraction_list)

# Если находить макс. и мин. не формулой, а вычислять через циклы, то понадобятся отдельные функции для макс. и мин.
# import random
# import math
# def fill_list(in_list: list, n: int) -> list:
#     '''
#     Возвращает список, заполненный случайными числами.

#         Args:
#             in_list (list) - пустой список
#             n (int) - число, которое задаёт пользователь, которое определяет размер списка  
#         Returns:
#             in_list (list) - список, заполненный случайными вещественными числами
#     '''
#     for i in range(0, n):
#         in_list.append(round((random.randint(0, 10) + random.random()), 5))
#     print(f'Исходный список: {in_list}')

# def form_fraction_list(in_list: list, n_list: list, n: int) -> list:
#     '''
#     Возвращает список, заполненный дробной частью элементов исходного списка.

#         Args:
#             in_list (list) - список, заполненный случайными вещественными числами
#             n_list (list) - пустой список
#             n (int) - число, которое задаёт пользователь, которое определяет размер списка  
#         Returns:
#             n_list (list) - список, заполненный дробной частью элементов исходного списка
#     '''
#     for i in range(0, n):
#         n_list.append(round((in_list[i] - math.floor(in_list[i])), 5))
#     print(f'Дробный список:  {n_list}')

# def find_min(n_list: list, n: int) -> float:
#     '''
#     Возвращает мин. значение дробной части элементов

#         Args:
#             n_list (list) - список, заполненный дробной частью элементов исходного списка
#             n (int) - размер списка  
#         Returns:
#             min (float) - мин. значение
#     '''
#     i = 0
#     min = n_list[i]
#     for i in range(1, n):
#         if n_list[i] < min:
#             min = n_list[i]
#             i += 1
#     return min

# def find_max(n_list: list, n: int) -> float:
#     '''
#     Возвращает макс. значение дробной части элементов

#         Args:
#             n_list (list) - список, заполненный дробной частью элементов исходного списка
#             n (int) - размер списка  
#         Returns:
#             max (float) - макс. значение
#     '''
#     i = 0
#     max = n_list[i]
#     for i in range(1, n):
#         if n_list[i] > max:
#             max = n_list[i]
#             i += 1
#     return max

# size = abs(int(input('Количество элементов в списке: ')))
# init_list = []
# fraction_list = []

# fill_list(init_list, size)
# form_fraction_list(init_list, fraction_list, size)
# diff = round((find_max(fraction_list, size) - find_min(fraction_list, size)), 5)
# print(f'Разница: {diff}')