def getInput():
    return open('input.txt')


def getInputAsInts():
    return [int(i) for i in getInput().read()]

def getInputAsCSVInts():
    return [int(i) for i in getInput().read().split(",")]