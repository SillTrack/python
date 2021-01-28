class Stationery:
    def __init__(self, stationery_title):
        self.title = stationery_title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисвки c помощью:', self.title)


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисвки c помощью:', self.title)


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисвки c помощью:', self.title)


pen = Pen('красная ручка')
pencil = Pencil('карандаш HB')
handle = Handle('фиолетовый маркер')
pen.draw()
pencil.draw()
handle.draw()



