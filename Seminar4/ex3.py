# Задайте последовательность чисел. Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности.

def search_repetition(list_):
    new_list = []
    for i in list_:
        if list_.count(i) == 1:
            new_list.append(i)
    return new_list


my_list = [4, 56, 4, 2, 1, 3]
print(f"Список элементов без повторений {set(my_list)}")
print(f"Cписок без элементов которые встречаются больше одного раза {search_repetition(my_list)}")

