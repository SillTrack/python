from sys import argv
script_name,  rate_per_hour, output_in_hours, premium = argv
print('Имя скрипта', script_name)
print('Ставка в час: ', rate_per_hour)
print('Выработка в часах: ', output_in_hours)
print('Премия: ', premium)
salary = int(output_in_hours) * int(rate_per_hour) + int(premium)
print('Заработная плата сотрудника составит:', salary)
