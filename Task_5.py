proceeds = 0
while proceeds <= 0:
    proceeds = int(input('Введите значение выручки фирмы: '))
costs = 0
while costs <= 0:
    costs = int(input('Введите значение издержек фирмы: '))
if proceeds > costs:
    print('Фирма отработала в прибыль')
    print('Рентабельность: %.3f' % ((proceeds-costs)/proceeds))
    number_of_employee = int(input('Введите куоличество работников: '))
    print('Прибыль фирмы в расчете на 1 сотрудника: %.3f' % ((proceeds-costs)/number_of_employee))
elif costs == proceeds:
    print('Фирма отработала в ноль')
else:
    print('Фирма отработала в убыток')