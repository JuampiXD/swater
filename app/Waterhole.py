from random import randrange


def drinkable():
    checker = randrange(2)
    return checker


class Waterhole:
    def __init__(self, length, latitude, size):
        self.length = length
        self.latitude = latitude
        self.size = size
        self.potable = drinkable()

    def extractinfo(self):
        expedition = {'length': self.length, 'latitude': self.latitude, 'size': self.size, 'potable': self.potable}
        return expedition
