class Cell:

    def __init__(self):
        self._coords = (0, 0)
        self._type = ""

    @property
    def coords(self):
        return self._coords

    @coords.setter
    def coords(self, value):
        self._coords = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
