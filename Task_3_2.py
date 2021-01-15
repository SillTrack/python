def function_output(name_var, surname_var, year_var, number_var, city_var, email_var):
    print(f'Имя - {name_var}, Фамиия - {surname_var}, Год рождения - {year_var}, Сотовый номер - {number_var}, Город проживания - {city_var}, email - {email_var}')


name = str(input('Введите имя пользователя: '))
surname = input('Введите фамилию пользователя: ')
year = input('Введите дату рождения пользователя: ')
while True:
    try:
        number = int(input('Введите телефон пользователя: '))
    except ValueError:
        print('Вводите все цифрами')
        continue
    break
city = input('Введите город проживания пользователя: ')
while True:
    email = input('Введите email пользователя: ')
    if email.find('@') > 0 and len(email) > 2 and email.find('.') > 0:
        break
    else:
        print('Введен неправильный формат email')
        continue

function_output(surname_var=surname, year_var=year, email_var=email, number_var=number, city_var=city, name_var=name)


