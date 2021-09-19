class IntervalList():
    """docstring for IntervalList."""

    def __init__(self):
        self.keys = []
        self.values = []

    def insert(self, key, value):
        position = len([i for i in self.keys if i < key])
        self.keys.insert(position, key)
        self.values.insert(position, value)

    def filterPosedge(self):
        res = IntervalList()
        for i in range(1, len(self.keys)):
            if ((self.values[i-1] == 0) and (self.values[i] > 0)):
                res.insert(i, 1)
        return res

    def filterNegedge(self):
        res = IntervalList()
        for i in range(1, len(self.keys)):
            if ((self.values[i-1] > 0) and (self.values[i] == 0)):
                res.insert(self.keys[i], 1)
        return res

    def filterInvert(self):
        res = IntervalList()
        for i in range(len(self.keys)):
                res.insert(self.keys[i], int(not bool(self.values[i])))
        return res

    def filterAnd(self, other):
        res = IntervalList()
        for i in range(len(self.keys)):
                res.insert(self.keys[i], int(not bool(self.values[i])))
        return res

    def filterOr(self, other):
        pass

    def filterXor(self, other):
        pass

    def filterLt(self, other):
        pass

    def filterLe(self, other):
        pass

    def filterEq(self, other, discriminant):
        res = IntervalList()
        for i in range(len(other.keys)):
            if(other.values[i] >= discriminant):
                res.insert(other.keys[i], self[i])
        return res

    def filterNeq(self, other):
        pass

    def filterGt(self, other):
        pass

    def filterGe(self, other):
        pass

    def __getitem__(self, key):
        position = len([i for i in self.keys if i <= key])
        return self.values[position-1]

    def __str__(self):
        res = "("
        for i in range(len(self.keys)):
            postfix = ", "
            value = self.values[i]
            lower = self.keys[i]
            try:
                upper = self.keys[i+1]-1
            except IndexError as e:
                upper = "Inf."
                postfix = ""
            res += ("[{0}, {1}] -> {2}"+postfix).format(lower, upper, value)
        res += ")"
        return res

    def __repr__(self):
        return self.__str__()
