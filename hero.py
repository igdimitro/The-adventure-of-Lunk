from entity import entity


class hero(entity):

    def __init__(self, name, attack, defence, agility):
        super().__init__(name, attack, defence, agility)
        self.__health = 100

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.__health = value
