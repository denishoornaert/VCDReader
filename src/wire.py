class Wire():
    """
    Class representing wires.
    """

    def __init__(self, bitwidth, id, name, values=None):
        self.bitwidth = bitwidth
        self.values = values
        self.name = name
        self.id = id

    def __str__(self):
        return "Wire(width : {0}, id : {1}, name : {2}) -> {3}".format(self.bitwidth, self.id, self.name, self.values.__str__()[:50])

    def __repr__(self):
        return self.__str__()
