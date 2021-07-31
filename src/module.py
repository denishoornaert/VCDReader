class Module():
    """
    Class representing modules.
    """

    def __init__(self, name=None, parent=None):
        self.name = name
        self.submodules = []
        self.wires = []
        self.parent = self if (parent == None) else parent

    def setName(self, name):
        self.name = name

    def addModule(self, module):
        self.submodules += [module]

    def addWire(self, wire):
        self.wires += [wire]

    def __str__(self):
        res = "Module {0}:\n".format(self.name)
        for wire in self.wires:
            res += "\t{0}\n".format(wire)
        for module in self.submodules:
            res += "{0}\n".format(module)
        return res.strip()
