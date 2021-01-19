while True:
    print('Чтобы выйти из программы введите q')
    user_str = input('Введите строку чисел через пробел: ')
    if user_str.find('q') > 0:
        flag = 1
        user_str = user_str.replace('q', '')
    else:
        flag = 0
    number_list = user_str.split()
    sum_of_numbers = 0
    try:
        for el in number_list:
            sum_of_numbers += int(el)
    except ValueError:
        print('Введите числа!')
        continue
    print('Сумма чисел в строчках:', sum_of_numbers)
    if flag == 1:
        break
    else:
        continue



