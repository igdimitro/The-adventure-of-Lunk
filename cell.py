class cell:

    def __init__(self):
        self.__coords = (0, 0)
        self.__type = ""

    @property
    def coords(self):
        return self.__coords

    @coords.setter
    def coords(self, value):
        self.__coords = value

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value
