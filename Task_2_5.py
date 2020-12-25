my_list = [7, 5, 3, 3, 2]
flag = 1
try_count = 0
max_try_count = 0
print('Текущий рейтинг:', my_list)
while flag != 0:
    if try_count == 0:
        try:
            max_try_count = int(input('Через сколько итераций необходимо остановить выполнение программы? '))
            if max_try_count < 0:
                print('Количество попыток не может быть отрицательным!')
                continue
        except ValueError:
            print('Введите число!')
            continue
    while True:
        try:
            user_number = int(input('Введите очередное число: '))
            break
        except ValueError:
            print('Введите число!')
            continue
    for el in my_list:
        if el < user_number:
            user_number_place = my_list.index(el)
            break
        else:
            temp = len(my_list)
    my_list.insert(user_number_place, user_number)
    print('Пользователь ввел число', user_number, '. Результат:', my_list)
    # my_list.insert(my_list.index(user_number-1),user_number)
    if try_count == max_try_count - 1:
        while True:
            try:
                flag = int(input('Введите 1 если хотите продолжить, или 0, если хотите остановится: '))
                if flag == 0 or flag == 1:
                    try_count = 0
                    break
            except ValueError:
                print('Введите цифру 1 или 0!')
                continue
    else:
        try_count += 1

