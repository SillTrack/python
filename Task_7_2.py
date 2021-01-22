from abc import abstractmethod


class Clothes:
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def cloth_calc(self):
        pass


class Coat(Clothes):
    @property
    def cloth_calc(self):
        return self.size/6.5 + 0.5

class Suit(Clothes):
    @property
    def cloth_calc(self):
        return 2*self.size + 0.3


print(Coat(6.5).cloth_calc)
print(Suit(3).cloth_calc)