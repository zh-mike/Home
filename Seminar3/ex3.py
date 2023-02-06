# Задайте список из вещественных чисел. Напишите программу которая найдет разницу
# между максимальным и минимальным значением дробной части
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def func(lst):
    new_lst = []
    for i in range(len(lst)):
        new_lst.append((lst[i] % 1))
    print(round(max(new_lst) - min(new_lst), 2))


my_lst = [1.1, 1.2, 3.1, 10.01]
func(my_lst)
