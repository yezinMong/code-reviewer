class Calc:
    def getSum(self, a, b):
        result = a + b
        return result

    def getGop(self, a, b):
        return a * b

    def getZegop(self, a):
        return a * a

    def getMinus(self, a, b):
        return a - b

    def getDivide(self, a, b):
        return 0 if b == 0 else a / b

    def getSumSum(self, a, b, c):
        return self.getSum(self.getSum(a, b), c)
