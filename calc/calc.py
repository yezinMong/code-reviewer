def getSum(a, b):
    result = a + b
    return result


def getGop(a, b):
    return a * b


def getZegop(a):
    pass


def getMinus(a, b):
    return a-b


def getDivide(a, b):
    return 0 if b == 0 else a / b


def getSumSum(a, b, c):
    return getSum(getSum(a, b), c)