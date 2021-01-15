with open('numbers', encoding='utf-8') as f_obj:
    # for str in f_obj:
    #     print(str, end='')
    with open('numbers_v2', 'w', encoding='utf-8') as f_obj_2:
        digits_dictionary = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
        while True:
            content = f_obj.readline()
            if not content:
                break
            content = content.split(' ')
            content[0] = digits_dictionary[content[0]]
            content = ' '.join(content)
            f_obj_2.write(content)
