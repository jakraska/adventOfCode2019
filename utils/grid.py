import re

class grid:
    data = []
    width = 0
    height = 0

    def __init__(self, width, height, initialFill):
        self.data = [[initialFill] * height for i in range(width)]
        self.width = width
        self.height = height

    def __iter__(self):
        return gridItr(self)

    def draw(self):
        for y in range(self.height):
            output = ''
            for x in range(self.width):
                output = output + str(self.data[x][y])
            print(output)



class gridItr:
    def __init__(self, grid):
        self.grid = grid
        self.x = 0
        self.y = 0

    def __next__(self):  # Python 2: def next(self)
        self.x += 1
        if self.x >= grid.width:
            self.y += 1
            self.x = 0
        if self.y >= grid.height:
            raise StopIteration

        return grid.data[self.x][self.y]


class point2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def fromString(cls, str):
        match = re.search('(\d+), (\d+)', str)

        return cls(int(match.group(1)), int(match.group(2)))

    def manhattanDistance(self, x, y):
        return abs(self.x - x) + abs(self.y - y)
