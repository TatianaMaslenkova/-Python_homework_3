# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний 
# элемент, второй и предпоследний и т.д. Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

import random
def fill_list(in_list: list, n: int) -> list:
    '''
    Возвращает список, заполненный случайными числами.

        Args:
            in_list (list) - список
            n (int) - число, которое задаёт пользователь, которое определяет размер списка  
        Returns:
            in_list (list) - список, заполненный случайными числами
    '''
    for i in range(0, n):
        in_list.append(random.randint(-10, 10))
    print(in_list)

def product_of_elements_pairs(in_list: list, n_list: list) -> list:
    '''
    Вычисляет произведения пар элементов.

        Args:
            in_list (list) - исходный список
            n_list (list) - пустой новый список
        Returns:
            n_list (list) - список, заполненный произведениями пар элементов исходного списка 
    '''
    i = 0
    end_num = -1
    half_len = len(in_list) / 2
    while i < half_len:
        n_list.append(in_list[i] * in_list[end_num])
        i += 1
        end_num -=1
    print(n_list)
   
size = abs(int(input('Количество чисел в списке: ')))
init_list = []
new_list = []

fill_list(init_list, size)
print('Произведение пар чисел списка равно: ')
product_of_elements_pairs(init_list, new_list)