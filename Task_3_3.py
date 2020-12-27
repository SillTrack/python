number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
number_3 = int(input('Введите третье число: '))
sum_of_max = sum([number_1, number_2, number_3]) - min([number_1, number_2, number_3])
print(sum_of_max)

