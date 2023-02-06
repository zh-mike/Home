# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


k = int(input())
fib_positive = [0, 1, 1]
fib_negative = [1, -1]

for i in range(2, k):
    fib_positive.append(fib_positive[-2] + fib_positive[-1])

for i in range(2, k):
    fib_negative.append(fib_negative[-2] - (fib_negative[-1]))

answer_list = [list(reversed(fib_negative)) + fib_positive]
print(answer_list)