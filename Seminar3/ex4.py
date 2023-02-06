# Напишите программу, которая будет преобразовывать 10 число в двоичные

def conv(number):
    new_num = ""
    while number > 0:
        new_num = str(number % 2) + new_num
        number //= 2
    return new_num

num = int(input("Введите число: "))
print(conv(num))

# print(bin(num))
