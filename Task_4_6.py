from itertools import count
from itertools import cycle

while True:
    try:
        flag = int(input('Введите 1 если хотите генерировать целые числа и 2, если хотите прокручивать список: '))
    except ValueError:
        print('Введите число ')
        continue
    break
if flag == 1:
    while True:
        try:
            user_number = int(input('Введите число с которого надо генерировать целые числа: '))
        except ValueError:
            print('Введите число ')
            continue
        break
    max_count = user_number + 30
    for el in count(user_number):
        if el > max_count:
            break
        else:
            print(el, end=' ')

if flag == 2:
    c = 0
    new_list = [12, 44, 4, 10, 78, 123]
    for el in cycle(new_list):
        if c > 3:
            break
        c += 1
        print(c, 'прокурутка листа', new_list)




