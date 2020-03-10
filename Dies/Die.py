from random import randrange


class Die:
    def __init__(self, sides):
        self.__sides = sides
        self.__value = None

    def get_sides(self):
        return self.__sides

    def get_value(self):
        return self.__value

    def roll(self):
        self.__value = randrange(1, self.__sides + 1)
