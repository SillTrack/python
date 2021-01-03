while True:
    try:
        number_of_month = int(input('Введите номер месяца: '))
    except ValueError:
        print('Введите целое число!')
        continue
    if number_of_month > 0 and number_of_month <= 12:
        break
    else:
        print('Отсчет месяцев идет от 1 до 12')
flag = None
while True:
    flag = int(input('Выберите способо решения задачи: 1 через словарь(dict), 0 - через список (list): '))
    if flag == 0 or flag == 1:
        break
if flag == 0:
    list_of_seasons = [0, 'зиме', 'зиме', 'весне', 'весне', 'весне', 'лету', 'лету', 'лету', 'осени', 'осени', 'осени', 'зиме']
    print(number_of_month, 'месяц относится к', list_of_seasons[number_of_month], 'задача решена через список(list)')
elif flag == 0:
    dict_of_seasons = {1: 'зимe', 2: 'зимe', 3: 'веснe', 4: 'веснe', 5: 'веснe', 6: 'лету', 7: 'лету', 8: 'лету', 9: 'осени', 10: 'осени', 11: 'осени', 12: 'зиме'}
    print(number_of_month, 'месяц относится к', (dict_of_seasons.get(number_of_month)), 'задача решена через словарь(dict)')

