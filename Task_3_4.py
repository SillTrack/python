def my_func(x, y):
    iterator = 1
    base = x
    while iterator < abs(y):
        x *= base
        iterator += 1
    return 1 / x


while True:
    try:
        number_base = int(input('Введите число x: '))
        number_exponent = int(input('Введите число y: '))
    except ValueError:
        print('Введите число!')
    if number_base > 0 > number_exponent:
        break
while True:
    try:
       flag = int(input('Введите 1 если программа должна быть выполнена через my_fync(x, y), 0 - иначе: '))
    except ValueError:
        print('Введите число!')
        continue
    if flag == 0 or flag == 1:
        break
if flag == 1:
    powered_x = my_func(number_base, number_exponent)
    print('Программа выполнена через my_fync(x, y), ответ:', powered_x)
else:
    print('Программа выполнена через оператор **, ответ:', number_base ** number_exponent)

