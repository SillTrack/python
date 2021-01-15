with open("staff", encoding='utf-8') as f_obj:
    salary = 0
    summ = 0
    number_of_stuff = 0
    for str in f_obj:
        salary = float(str.split(' ')[1])
        if salary < 20000:
            print(str.strip())
        summ += salary
        number_of_stuff += 1
print('Средняя зарплата всех рабочих составляет:', '%.3f' % (summ/number_of_stuff))