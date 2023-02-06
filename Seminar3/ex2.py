# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def f(lst):
    result_list = []
    while len(lst) > 1:
        result_list.append(lst.pop(0) * lst.pop())
        if len(lst) == 1:
            result_list.append(lst[0]**2)
    return result_list


my_list_1 = [2, 3, 4, 5, 6]
my_list_2 = [2, 3, 5, 6]

print(f(my_list_1))
