import utils.input
from typing import Type  # you have to import Type

class planet:
    def __init__(self, name:str):
        self.name = name
        self.orbiters = []
        self.parent = None

    def addOrbiter(self, other: 'planet'):
        self.orbiters.append(other)

    def set_parent(self, other: 'planet'):
        self.parent = other

    def total_orbits(self) -> int:
        sum = len(self.orbiters)
        for other in self.orbiters:
            sum += other.total_orbits() + other.total_children()
        return sum

    def total_children(self) -> int:
        sum = len(self.orbiters)
        for other in self.orbiters:
            sum += other.total_children()
        return sum

    def dist_to(self, target:str) -> int:
        if self.name == target:
            return 0

        for o in self.orbiters:
            d = o.dist_to(target)
            if d >= 0:
                return d + 1

        return -1

def part1(center: planet):
    print(center.total_orbits())
    return

def part2(you: planet):
    n = you.parent
    dist = 0
    while n is not None:
        dist = n.dist_to("SAN")
        if dist >= 0:
            break
        n = n.parent

    dist += n.dist_to("YOU")
    dist -= 2
    print(dist)

    return

def parse_planets(ret_planet:str = None) -> planet:
    planets = {}
    possible_coms = {}
    for row in utils.input.getInput().readlines():
        center = row[0:3]
        orbiter = row[4:7]

        if planets.get(center) is None:
            planets[center] = planet(center)
            possible_coms[center] = planets.get(center)

        if planets.get(orbiter) is None:
            planets[orbiter] = planet(orbiter)
        else:
            possible_coms.pop(orbiter)

        planets[center].addOrbiter(planets.get(orbiter))
        planets.get(orbiter).set_parent(planets.get(center))

    if ret_planet is None:
        for key, value in possible_coms.items():
            return value
    else:
        return planets.get(ret_planet)



# part1(parse_planets())
part2(parse_planets("YOU"))