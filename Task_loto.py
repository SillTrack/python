import random


def sort_for_increase(list_of_str):
    temp = []
    i = 0
    list_of_str = [str(el) for el in list_of_str]
    for el in list_of_str:
        if el != '  ':
            temp.append(int(el))
    temp = sorted(temp)
    for el in list_of_str:
        if el != '  ':
            list_of_str.insert(list_of_str.index(el), temp[i])
            list_of_str.remove(el)
            i += 1
    return list_of_str


class LotoCard:

    def __init__(self, player_name):
        self.name = player_name
        self.card_list = []
        self.card = ''


    def card_generate(self):
        robj = list(range(1, 91))
        for i in range(15):
            self.card_list.append(random.choice(robj))
            robj.remove(self.card_list[i])
        card_list_copy = self.card_list.copy()
        self.card_list.clear()
        temp_list = []
        temp_list_space = ['  ', '  ', '  ', '  ']
        while len(card_list_copy) > 0:
            temp_list.append(card_list_copy.pop(0))
            if len(card_list_copy) % 5 == 0:
                temp_list += temp_list_space
                random.shuffle(temp_list)
                temp_list = sort_for_increase(temp_list)
                self.card_list += temp_list
                temp_list.clear()
        return self.card_list  # список с интами и пробелами




    def remove_number(self, number):
        if self.card_list.count(number) > 0:
            self.card_list.insert(self.card_list.index(number), ' -')
            self.card_list.remove(number)
            return 1
        else:
            return 0

    def __str__(self):
        card = ''
        card_list_copy = self.card_list.copy()
        card_list_copy = [str(el).ljust(2, ' ') for el in card_list_copy]  # int в str
        while len(card_list_copy) > 0:
            card += card_list_copy.pop(0) + ' '
            if len(card_list_copy) % 9 == 0:
                card += '\n'
        self.card = card
        return f"{self.name}:" + '\n' + '--------------------------' + '\n' + self.card + '--------------------------'


class LotoGame:
    def __init__(self, player_card, computer_card):
        self.computer_card = computer_card
        self.player_card = player_card

    def start(self):
        computer_right_answer = 0
        player_right_answer = 0
        temp = 0
        robj = list(range(1, 91))
        while computer_right_answer < 15 and player_right_answer < 15:
            temp = random.choice(robj)
            robj.remove(temp)
            print(self.computer_card)
            print(self.player_card)
            print(f"выпал бочонок {temp}, осталось {len(robj)}")
            choice = input('Хотите зачеркнуть? y/n:\n')
            while choice != 'y' or choice != 'n':
                choice = input('Хотите зачеркнуть? y/n:\n')
            computer_right_answer += self.computer_card.remove_number(temp)
            if choice == 'y':
                if self.player_card.remove_number(temp) == 0:
                    print('Вы проирали! Такого числа нет в вашей карточке.')
                    break
                else:
                    player_right_answer += 1
            else:
                if self.player_card.remove_number(temp) == 0:
                    print(self.player_card)
                else:
                    print('Вы проирали! Вы не зачеркнули бочонок!')
                    break






lotocard = LotoCard('Иван')
lotocard.card_generate()
computer_card = LotoCard('Компьютер')
computer_card.card_generate()
game = LotoGame(lotocard, computer_card)
game.start()
