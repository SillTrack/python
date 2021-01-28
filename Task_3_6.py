def int_func(word):
    new_list = word.split()
    for el in new_list:
        if new_list.index(el) < len(new_list):
            new_list[new_list.index(el)] = new_list[new_list.index(el)].title()
    return new_list


user_str = input('Введите слово: ')
print(' '.join(int_func(user_str)))



