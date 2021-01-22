flag = 0
list_of_products = []
index_of_product = 0
name_of_product = 0
list_of_name = []
price_of_product = 0
list_of_price = []
number_of_product = 0
list_of_number = []
product_unit = 0
list_of_unit = []
try_count = 1
max_try_count = int(input('Введите количество товаров, которое необходимо проанализировать: '))
temp_list = []
while try_count <= max_try_count:
    index_of_product += 1
    temp_list.append(index_of_product)
    name_of_product = input('Введите название'' товара: ')  # проверка является ли строкой + добавить , index_of_product,
    list_of_name.insert(try_count, name_of_product)
    while True:
        try:
            price_of_product = int(input('Введите цену за'' товар: '))  # проверка является ли числом
        except ValueError:
            print('Введите число!')
            continue
        if price_of_product > 0:
            break
        else:
            print('Введите положительное число! Цена товара не может быть отрицательной!')
    list_of_price.insert(try_count, price_of_product)
    while True:
        try:
            number_of_product = int(input('Введите количество'' товара: '))  # проверка является ли числом
        except ValueError:
            print('Введите число!')
            continue
        if number_of_product >= 0:
            break
        else:
            print('Введите неотрицательное число! Количество товара не может быть меньше нуля!')
    list_of_number.insert(try_count, number_of_product)
    product_unit = input('Введите единицу измерения' ' товара (шт., кг, м и тд.): ')
    list_of_unit.insert(try_count, product_unit)
    dict_of_product = {'название': name_of_product, 'цена': price_of_product, 'количество': number_of_product, 'ед.': product_unit}
    temp_list.append(dict_of_product)
    new_tuple = tuple(temp_list)
    print('Полученный кортеж:', new_tuple)
    list_of_products.insert(try_count, new_tuple)
    temp_list.clear()
    try_count += 1
print('***********************************************************************************************')
print('Готовая структура ВСЕХ товаров:')
for el in list_of_products:
    print(el)
analysis_dict = {'название': list_of_name, 'цена': list_of_price, 'количество': list_of_number, 'ед.': list_of_unit}
print('***********************************************************************************************')
print('Собранная аналитика ВСЕХ товаров:')
for key, value in analysis_dict.items():
    print(f"{key}  {value}")


