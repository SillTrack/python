n = int(input('Введите число n: '))
answer = n + (n*10 + n) + (n*100 + n*10 + n)
print ('Сумма числе n + nn + nnn: ')
print (f"{n} + {(n*10 + n)} + {(n*100 + n*10 + n)} = {answer}")