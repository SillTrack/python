with open('Subjects', encoding='utf-8') as f_obj:
    new_dict = {}
    string = f_obj.readline()
    while len(string) > 0:
        numbers = 0
        while string.find('(') > 0:
            temp = string[string.find(' '): string.find('(')]
            if temp.find('—') > 0:
                temp = temp.replace(temp[0: temp.find('—')+2], '')
            numbers += int(temp)
            string = string.replace(string[string.find(' '): string.find(')')+1], '')
        temp = string[0: string.index(':')]
        new_dict = {string[0: string.index(':')]: numbers}
        print(new_dict)
        string = f_obj.readline()
