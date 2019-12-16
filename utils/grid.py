import re
import math
from typing import List


class HashGridData:
    pos = None
    value = None

    def __init__(self, x:int, y:int, value):
        self.pos = point2d(x, y)
        self.value = value

    def __repr__(self):
        return "%s: %s" % (self.pos, self.value)


class HashGrid:
    default_value = None
    data = {}

    def __init__(self, default_value, initial_data:List[HashGridData] = None):
        self.default_value = default_value
        self.data = {}

        if initial_data is not None:
            for d in initial_data:
                self.data[d.pos.__repr__()] = d

    def set_value(self, x:int, y:int, val):
        d = HashGridData(x, y, val)
        self.data[d.pos.__repr__()] = d

    def get_value(self, x, y):
        d = self.data.get(point2d(x,y).__repr__())
        return self.default_value if d is None else d.value

    def remove_value(self, x, y):
        self.data.pop(point2d(x,y).__repr__())

    def get_data(self):
        return list(self.data.values())

    def find(self, val) -> List[HashGridData]:
        return list(filter(lambda d: d.value == val, self.data.values()))

    def as_string(self, invert:bool = False, output_map=None, output_map_default=" "):
        # todo cache this on set/remove
        minx = min(self.data.values(), key=lambda d: d.pos.x).pos.x
        maxx = max(self.data.values(), key=lambda d: d.pos.x).pos.x
        miny = min(self.data.values(), key=lambda d: d.pos.y).pos.y
        maxy = max(self.data.values(), key=lambda d: d.pos.y).pos.y

        y_start, y_end, y_step = (miny, maxy + 1, 1) if invert else (maxy, miny - 1, -1)
        output = ""
        for y in range(y_start, y_end, y_step):
            for x in range(minx, maxx + 1):
                v = str(self.get_value(x, y))
                if output_map is not None:
                    v = output_map.get(v, output_map_default)
                output += v
            output += "\n"
        return output


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

class point3d:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __repr__(self):
        return "(%s,%s,%s)" % (self.x, self.y, self.z)

    @classmethod
    def fromString(cls, str):
        match = re.search('<x=(-?\d+), y=(-?\d+), z=(-?\d+)>', str)

        return cls(int(match.group(1)), int(match.group(2)), int(match.group(3)))

    def manhattanDistance(self, x, y, z):
        return abs(self.x - x) + abs(self.y - y) + abs(self.z - z)

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


