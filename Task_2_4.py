new_str = input('введите строку со словами, ставя между ними пробелы: ')
for ind, el in enumerate(new_str.split(), 1):
    if len(el) > 10:
        print(ind, el[0:10].title())
    else:
        print(ind, el.title())
