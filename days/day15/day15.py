import utils.input
from utils.grid import HashGrid, point2d
from days.day11.intcode_computer import intcode_computer
from typing import List

d = {
    1: point2d(0, 1),
    2: point2d(0, -1),
    3: point2d(-1,0),
    4: point2d(1,0)
}
do = {
    1:2,
    2:1,
    3:4,
    4:3
}

out_map = {
    "-2": "S",
    "-1": " ",
    "0": "#",
    "1": ".",
    "2": "C"
}
def part1():
    ic = intcode_computer(utils.input.getInputAsCSVInts())
    g = HashGrid(-1)
    g.set_value(0,0, 1)

    map_world(ic, g, point2d(0,0), 0)
    g.set_value(0,0, -2)
    print(g.as_string(output_map=out_map))
    return

def map_world(ic: intcode_computer, g: HashGrid, pos:point2d, depth:int):
    for dir_code in d:
        next_pos = point2d(pos.x + d[dir_code].x, pos.y + d[dir_code].y)
        if g.get_value(next_pos.x, next_pos.y) == -1:
            ic.execute([dir_code])
            o = ic.pop_output()[0]
            g.set_value(next_pos.x, next_pos.y, o)
            if o == 1 or o == 2:
                map_world(ic, g, next_pos, depth +1)
                ic.execute([do[dir_code]])
                ic.pop_output()
                if(o==2):
                    print(depth+1)


def part2():
    ic = intcode_computer(utils.input.getInputAsCSVInts())
    g = HashGrid(-1)
    g.set_value(0, 0, 1)

    map_world(ic, g, point2d(0, 0), 0)
    s = g.find(2)[0]
    time = spread_oxygen(g, [s.pos], 0)
    print(time)
    return

def spread_oxygen( g: HashGrid, locations: List[point2d], depth:int):
    new_locations = []
    for l in locations:
        for direction in d.values():
            p = point2d(l.x + direction.x, l.y + direction.y)
            if g.get_value(p.x, p.y) == 1:
                new_locations.append(p)
                g.set_value(p.x, p.y, 2)

    if len(new_locations) == 0:
        return depth
    else:
        return spread_oxygen(g, new_locations, depth+1)


part2()
