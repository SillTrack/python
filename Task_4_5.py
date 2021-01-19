from functools import reduce


def my_func(prev_el, el):
    return prev_el * el


new_list = [i for i in range(100, 1001, 2)]
print(new_list)
print(reduce(my_func, new_list))