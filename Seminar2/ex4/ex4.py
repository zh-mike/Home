# 4) Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение
#    элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint
n = int(input("Введите количество элементов: "))
list_num = []

for _ in range(n):
    list_num.append(randint(-n, n))
print(list_num)

sum = 1
my_path = 'GB_Python/Home/Seminar2/ex4/file.txt'
with open(my_path) as my_index:
    for i in my_index:
        try:
            sum *= list_num[int(i)]
        except:
            print('Индекс не найден')

print(sum)
