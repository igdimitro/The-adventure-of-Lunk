from cell import cell


class entity(cell):

    def __init__(self, name, attack, defence, agility):
        super().__init__()
        self.__name = name
        self.__attack = attack
        self.__defence = defence
        self.__agility = agility

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def attack(self):
        return self.__attack

    @attack.setter
    def attack(self, value):
        self.__attack = value

    @property
    def defence(self):
        return self.__defence

    @defence.setter
    def defence(self, value):
        self.__defence = value

    @property
    def agility(self):
        return self.__agility

    @agility.setter
    def agility(self, value):
        self.__agility = value
