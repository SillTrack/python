import json


with open('Firms', encoding='utf-8') as f_obj:
    string = f_obj.readline().strip()
    profit = 0
    average_profit = 0
    num_of_firms = 0
    new_list = []
    while len(string) > 0:
        string = string.split('  ')
        profit = int(string[2]) - int(string[3])
        if profit > 0:
            average_profit += profit
            num_of_firms += 1
        new_list.append({string[0]: profit})
        string = f_obj.readline().strip()
    new_list.append({'average_profit': '%.2f' % (average_profit/num_of_firms)})
    print(new_list)
    with open("my_file.json", "w") as write_f:
        json.dump(new_list, write_f)