import utils.input
from utils.grid import point2d, line2d
from typing import List



def parseAsVectors(csvStr:str):
    vectors = []
    for move in csvStr.split(","):
        if move[0] == "R":
            vectors.append(point2d(int(move[1:]), 0))
        elif move[0] == "L":
            vectors.append(point2d( -1 * int(move[1:]), 0))
        elif move[0] == "U":
            vectors.append(point2d( 0, int(move[1:])))
        elif move[0] == "D":
            vectors.append(point2d( 0, -1 * int(move[1:])))

    return vectors


def vectorsToLines(vectors):
    lines = []
    start = point2d(0, 0)
    for i in range(len(vectors)):
        end = point2d(start.x + vectors[i].x, start.y + vectors[i].y)
        lines.append(line2d(point2d(start.x, start.y), point2d(end.x, end.y)))
        start = end
    return lines


def part1(path_a:List[line2d], path_b:List[line2d]):
    intersects = []
    for a in path_a:
        for b in path_b:
            x = a.get_intersection(b)
            if x is not None:
                intersects.append(x)

    closest = min(intersects, key=lambda x: x.manhattanDistance(0,0))
    print(closest.manhattanDistance(0,0))


def distToPoint(path:List[line2d], point:point2d):
    dist = 0
    for line in path:
        if line.contains(point):
            dist += point.manhattanDistance(line.start.x, line.start.y)
            return dist
        else:
            dist += line.length()
    return None

def part2(path_a:List[line2d], path_b:List[line2d]):
    intersects = []
    for a in path_a:
        for b in path_b:
            x = a.get_intersection(b)
            if x is not None:
                intersects.append(x)

    min_dist = None
    for pt in intersects:
        da = distToPoint(path_a, pt)
        db = distToPoint(path_b, pt)
        d = da+db

        min_dist = d if min_dist is None else min(min_dist, d)

    print(min_dist)

i = utils.input.getInput()
a = vectorsToLines(parseAsVectors(i.readline()))
b = vectorsToLines(parseAsVectors(i.readline()))

part2(a, b)