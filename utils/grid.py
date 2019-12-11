import re
import math

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

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "(%s,%s)" % (self.x, self.y)

    @classmethod
    def fromString(cls, str):
        match = re.search('(\d+), (\d+)', str)

        return cls(int(match.group(1)), int(match.group(2)))

    def manhattanDistance(self, x, y):
        return abs(self.x - x) + abs(self.y - y)

class line2d:
    def __init__(self, start:point2d, end:point2d):
        self.start = start
        self.end = end


    def get_intersection(self, other):
        horizontal, vertical = None, None
        if self.start.x - self.end.x == 0 and other.start.y - other.end.y == 0:
            vertical, horizontal = self, other
        elif self.start.y - self.end.y == 0 and other.start.x - other.end.x == 0:
            horizontal, vertical = self, other
        else:
            return None

        if  min(vertical.start.y, vertical.end.y) < horizontal.start.y < max(vertical.start.y, vertical.end.y) \
                and min(horizontal.start.x, horizontal.end.x) < vertical.start.x < max(horizontal.start.x, horizontal.end.x):
            return point2d(vertical.start.x, horizontal.start.y)
        return None

    def contains(self, pt:point2d):
        return min(self.start.y, self.end.y) <= pt.y <= max(self.start.y, self.end.y) \
            and min(self.start.x, self.end.x) <= pt.x <= max(self.start.x, self.end.x)

    def length(self):
        return self.start.manhattanDistance(self.end.x, self.end.y)


