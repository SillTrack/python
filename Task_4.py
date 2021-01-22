user_number = 0
while user_number <= 0:
    user_number = int(input('Введите положительное число для определения наибольшей цифры в нем: '))
print('Введенное число:', user_number)
max_digit = user_number % 10
user_number = user_number // 10
while user_number > 0:
    temp = user_number % 10
    user_number = user_number // 10
    if temp > max_digit:
        max_digit = temp
print('Самая большая цифра в веденном числе:', max_digit)
