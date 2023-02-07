# 4) Задана натуральная степень k. Сформировать случайным образом список коэффицентов (значения от 0 до 100)
#  многочлена и записать в файл многочлен степени k
from random import randint
f_path = 'Seminar4/ex4/answer_file.txt'
k = int(input('Введите степень k: '))
text = "= 0"
for i in range(0, k+1):
    polynomial = str(randint(0, 10))
    if polynomial == '1' and i >0:
        text = f'+ X**{i} {text}'
    elif polynomial != '0':
        if i == 0:
            text = f'+ {polynomial} {text}'
        elif i == 1:
            text = f'+ {polynomial}*X {text}'
        else:
            text = f'+ {polynomial}*(X**{i}) {text}'
print(text[2:])
with open(f_path, 'a') as my_print:
    my_print.writelines(f'{text[2:]}\n')