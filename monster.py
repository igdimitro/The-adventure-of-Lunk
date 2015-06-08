from entity import Entity


class Monster(Entity):

    def __init__(self, name, attack, defence, agility, health):
        super().__init__(name, attack, defence, agility)
        self.__health = health

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.__health = value
