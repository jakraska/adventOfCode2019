def getInput():
    return open('input.txt')


def getInputAsInts():
    return [int(i) for i in getInput()]

def getInputAsCSVInts():
    return [int(i) for i in getInput().read().split(",")]