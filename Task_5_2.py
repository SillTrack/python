# f_fobj = open('out_file.txt')
import itertools


with open('out_file.txt') as f_obj:
    for str in enumerate(f_obj, 1):
        num_of_words = len(str[1].split(' '))
        # for el in str[1]:
        #     if el == ' ':
        #         num_of_words += 1
        temp = str[1]
        print(str[0], 'строка -', temp.strip(), 'содержит: ', num_of_words, ' слов.')
