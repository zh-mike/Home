# 1) Вычислить число с задоной точкой d

import math
pi = math.pi
# p = 3.1415926535
d = input('Введите число: ')
d = d.split('.')[1]
print(round(pi, (len(d))))
# print(pi)