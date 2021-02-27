from abc import ABC, abstractmethod


class Clothes:
    def __init__(self, name, param=None):
        self.name = name
        self.param = param

    @abstractmethod
    def get_consumption(self):
        pass


class Coat(Clothes):
    @property
    def get_consumption(self):
        return round(self.param / 6.5 + 0.5, 2)


class Suit(Clothes):
    @property
    def get_consumption(self):
        return round(2 * self.param + 0.3, 2)


boss = Coat('boss', 100)
print(boss.get_consumption)
not_boss = Suit('not_boss', 80)
print(not_boss.get_consumption)
