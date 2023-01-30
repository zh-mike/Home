# Реализуйте алгоритм перемешивания списка.

from random import randint

list_a = [1, 2, 3, 4, 5]
print(f"Начальный Лист a {list_a}")
list_b = []
count = len(list_a)-1
element = 0
for _ in range(len(list_a)):
    el = randint(0, count)
    list_b.append(list_a[el])
    list_a.pop(el)
    count -= 1
print(f"Финальный Лист b {list_b}")