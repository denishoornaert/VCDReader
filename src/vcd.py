class VCD():
    """docstring for VCD."""

    def __init__(self):
        self.idToValues = dict()
        self.nameToId = dict()
        self.topModule = None

    def select(self, field):
        return self.idToValues[self.nameToId[field]]
