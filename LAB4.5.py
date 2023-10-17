# < Іваньо Іван >
# Лабораторна робота № 4.5
# «Попадання» у плоску фігуру.
# Варіант 0.6

import random

R = int(input("R: "))
i = 1

while i <= 10:
    print("Постріл №"+str(i)+" ")
    x = int(input("x: "))
    y = int(input("y: "))
    if ((x ** 2 + y ** 2 <= R ** 2) and y >= 0) or ((x ** 2 + y ** 2 >= R ** 2) and 0 > y > -R and -R < x < 0):
        print('YES')
    else:
        print('NO')
    i += 1

i = 1

while i <= 10:
    x = random.randrange(-2 * R, 2 * R + 1)
    y = random.randrange(-2 * R, 2 * R + 1)
    if ((x ** 2 + y ** 2 <= R ** 2) and y >= 0) or ((x ** 2 + y ** 2 >= R ** 2) and 0 > y > -R and -R < x < 0):
        print(str(x), str(y) + ' YES')
    else:
        print(str(x), str(y) + ' NO')
    i += 1
