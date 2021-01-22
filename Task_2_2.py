while True:
    try:
        number_of_elements = int(input('Введите количество элементов списка: '))
    except ValueError:
        print('Введите число!')
        continue
    if number_of_elements > 0:
        break
iterator = 0
my_list = []
reverse_my_list = []
while iterator != number_of_elements:
    try:
        temp = (input('Введите очередной элемент списка '))
        my_list.append(int(temp))
    except ValueError:
        my_list.append(str(temp))
    iterator += 1
iterator = 0
my_list.reverse()
reverse_my_list.extend(my_list)
my_list.reverse()
print('Список, который ввел пользователь:', my_list)
while number_of_elements - iterator != 1 and number_of_elements - iterator != 0:
    print('Меняем', my_list[iterator], 'и', my_list[iterator + 1], 'местами:')
    my_list.pop(iterator)
    my_list.pop(iterator)
    my_list.insert(iterator, reverse_my_list[number_of_elements - (iterator + 1)])
    my_list.insert(iterator, reverse_my_list[number_of_elements - (iterator + 2)])
    print('Вот что получилось', my_list)
    iterator += 2
print('Измененный список', my_list)
