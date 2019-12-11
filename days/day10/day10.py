import utils.input
import math
from typing import List
from utils.grid import point2d



def part1():
    asteroids = parse_input()
    m = max(asteroids, key=lambda x:len(calc_visible(asteroids, x)) )
    visible = calc_visible(asteroids, m)

    # for a in asteroids:
    #     print(len(calc_visible(asteroids, a)))
    print(len(visible))
    print("x:%s, y:%s" % (m.x, m.y))
    return




def blocks_view(station:point2d, a:point2d, b:point2d):
    av = get_normal_vector(station, a)
    bv = get_normal_vector(station, b)
    return math.isclose(av.x, bv.x) and math.isclose(av.y, bv.y)
def vector_is_close(av:point2d, bv:point2d):
    return math.isclose(av.x, bv.x) and math.isclose(av.y, bv.y)

def get_normal_vector(a:point2d, b:point2d):
    m = math.sqrt(math.pow(a.x - b.x, 2) + math.pow(a.y - b.y, 2))
    ratio = float(1) / m
    return point2d((a.x - b.x)*ratio,(a.y - b.y)*ratio)

def parse_input():
    asteroids = []
    data = utils.input.getInput().readlines()
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == "#":
                asteroids.append(point2d(x, y))
    return asteroids

def calc_visible(asteroids:List[point2d], center:point2d):
    visible_asteroid_vectors = []

    for a in asteroids:
        if a == center:
            continue
        v = get_normal_vector(center, a)
        visible = True
        for b in visible_asteroid_vectors:
            if vector_is_close(v, b):
                visible = False
                break

        if visible:
            visible_asteroid_vectors.append(v)
    return visible_asteroid_vectors


def part2():
    asteroids = parse_input()
    base = point2d(22, 19)
    up = point2d(0, -1)
    asteroids.remove(base)

    known_angles = []

    for a in asteroids:
        angle = angle_between(up, point2d(a.x - base.x, a.y - base.y))
        found = False
        for k in known_angles:
            if math.isclose(angle, k[0]):
                k[1].append(a)
                found = True
                break
        if not found:
            known_angles.append((angle, [a]))

    # sort the angles
    known_angles.sort(key=lambda x : x[0])

    #sort based on distance
    for k in known_angles:
        k[1].sort(key=lambda a: base.manhattanDistance(a.x, a.y))

    i = 0
    count = 0
    while count < 200:
        if len(known_angles[i][1]) > 0:
            a = known_angles[i][1].pop()
            count += 1
            print("%s: (%s, %s)" % (count, a.x, a.y))
        i += 1
        if i >= len(known_angles):
            i = 0

    return


def angle_between(a:point2d, b:point2d):
    angle = math.atan2(b.y, b.x) - math.atan2(a.y, a.x)
    return angle + (math.pi * 2) if angle < 0 else angle

part2()
