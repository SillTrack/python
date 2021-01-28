import math


def fact(n):
    for el in range(1,n+1):
        yield math.factorial(el)


while True:
    try:
        user_number = int(input('Введите число до которого необходимо выводить факториал: '))
    except ValueError:
        print('Введите положительное число')
    if user_number <= 0:
        continue
    else:
        break
for el in fact(user_number):
    print(el, end=' ')
