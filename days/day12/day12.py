import utils.input
from utils.grid import point3d, HashGrid
from typing import List
import math


class Planet:
    def __init__(self, pos:point3d, vel:point3d):
        self.pos = pos
        self.vel = vel

    def apply_gravity(self, other:'Planet'):
        self.vel.x += acceleration_val(self.pos.x, other.pos.x)
        self.vel.y += acceleration_val(self.pos.y, other.pos.y)
        self.vel.z += acceleration_val(self.pos.z, other.pos.z)

    def apply_velocity(self):
        self.pos.x += self.vel.x
        self.pos.y += self.vel.y
        self.pos.z += self.vel.z

    def get_energy(self):
        return (abs(self.pos.x) + abs(self.pos.y) + abs(self.pos.z)) * (abs(self.vel.x) + abs(self.vel.y) + abs(self.vel.z))

    def __repr__(self):
        return "pos=%s, vel=%s" % (self.pos, self.vel)


def part1(planets:List[Planet]):
    for t in range(1000):
        time_tick(planets)
    energy = sum(p.get_energy() for p in planets)
    print(energy)
    return

def part2(planets:List[Planet]):
    past = {}
    lastX = 0
    for t in range(10000000):
        time_tick(planets)
        p = planets[0]
        print("%s: lastXDiff: %s"%(p.pos, p.pos.x-lastX))
        lastX = p.pos.x
        # k = "%s" % (p.pos)
        # if k in past:
        #     print("dupe %s  %s,  at:  %s, " % (p.pos, p.vel, t))
        # else:
        #     past[k] = True

    # energy = sum(p.get_energy() for p in planets)
    # print(energy)

    return

def time_tick(planets:List[Planet]):
    for p in planets:
        for other in planets:
            p.apply_gravity(other)

    for p in planets:
        p.apply_velocity()

def acceleration_val(a:int, b:int):
    if a == b:
        return 0

    return 1 if b > a else -1



planets = [ Planet(point3d.fromString(s.strip()), point3d(0,0,0)) for s in  utils.input.getInput().readlines()]

part2(planets)