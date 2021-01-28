while True:
    try:
        user_number_1 = float(input('Введите первое число: '))
    except ValueError:
        print('Введите число!')
        continue
    try:
        user_number_2 = float(input('Введите второе число: '))
    except ValueError:
        print('Введите число!')
        continue
    break
try:
    print('Отношение чисел: ', user_number_1 / user_number_2)
except ZeroDivisionError:
    print('Деление на нуль!')