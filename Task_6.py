a = 0
b = 0
while a <= 0 and b <= 0:
    a = int(input('Введите результат пробежки спортсмена за 1 день: '))
    b = int(input('Введите результат которого должен достичь спортсмен: '))
number_of_day = 1
print(number_of_day, 'день:', a)
while a < b:
    number_of_day += 1
    a += a*0.1
    print(number_of_day, 'день: %.2f' % a)
print('Ответ: на', number_of_day, 'день спортсмен достиг резудьтата не менее', b, 'км')
