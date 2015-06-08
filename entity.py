from cell import Cell


class Entity(Cell):

    def __init__(self, name, attack, defence, agility):
        super().__init__()
        self._name = name
        self._attack = attack
        self._defence = defence
        self._agility = agility

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def attack(self):
        return self._attack

    @attack.setter
    def attack(self, value):
        self._attack = value

    @property
    def defence(self):
        return self._defence

    @defence.setter
    def defence(self, value):
        self._defence = value

    @property
    def agility(self):
        return self._agility

    @agility.setter
    def agility(self, value):
        self._agility = value
