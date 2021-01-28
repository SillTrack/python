out_f = open('out_file.txt', 'w')
str_list = []
while True:
    str_line = input('Введите очередную строку: ') + '\n'
    if str_line == '':
        print('Запись в файл окончена. Конец программы')
        break
    out_f.writelines(str_line)
out_f.close()