import io

sum_of_elements = 0
with open('digits', 'w') as f_obj:
    f_obj.write(input('Введите набор чисел раздеоленных пробелами: '))
with open('digits', 'r') as f_obj:
    str = f_obj.readline()
    str = str.strip().split(' ')
    for el in str:
        sum_of_elements += float(el)
    print('сумма чисел равна:', sum_of_elements)
