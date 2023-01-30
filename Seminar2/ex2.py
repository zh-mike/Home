# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

num = int(input("-> "))
sum = 1
text_list = []
for i in range(1, num + 1):
    sum *= i
    text_list.append(sum)
print(text_list)
