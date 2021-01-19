original_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = []
new_list = [el for el in original_list if el > original_list[original_list.index(el) - 1]]
new_list.pop(0)
print(new_list)
