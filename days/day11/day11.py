import utils.input
import math
from utils.grid import point2d
from days.day11.intcode_computer import intcode_computer

def rotate(vector:point2d, turn:int):
    angle = (math.pi / 2) if turn == 0 else -1 *(math.pi / 2)
    sin = int(math.sin(angle))
    cos = int(math.cos(angle))
    return point2d(vector.x * cos - vector.y * sin, vector.y * cos + vector.x * sin )

def part1(computer:intcode_computer):
    pos = point2d(0,0)
    forward = point2d(0,1)
    tiles = {}
    while not computer.is_complete:
        cur_tile = tiles.get(pos.__repr__())
        curr_color = 0 if cur_tile is None else cur_tile[1]
        computer.execute([curr_color])
        tiles[pos.__repr__()] = (point2d(pos.x, pos.y), computer.output.pop(0))
        turn = computer.output.pop(0)
        forward = rotate(forward, turn)
        pos.x += forward.x
        pos.y += forward.y

    print(len(tiles))
    return

def part2(computer:intcode_computer):
    pos = point2d(0, 0)
    forward = point2d(0, 1)
    tiles = {}
    tiles[pos.__repr__()] = (point2d(pos.x, pos.y), 1)
    while not computer.is_complete:
        cur_tile = tiles.get(pos.__repr__())
        curr_color = 0 if cur_tile is None else cur_tile[1]
        computer.execute([curr_color])
        tiles[pos.__repr__()] = (point2d(pos.x, pos.y), computer.output.pop(0))
        turn = computer.output.pop(0)
        forward = rotate(forward, turn)
        pos.x += forward.x
        pos.y += forward.y

    minx = min(tiles.values(), key=lambda t:t[0].x)[0].x
    maxx = max(tiles.values(), key=lambda t:t[0].x)[0].x
    miny = min(tiles.values(), key=lambda t:t[0].y)[0].y
    maxy = max(tiles.values(), key=lambda t:t[0].y)[0].y

    output = ""
    for y in range(maxy, miny-1, -1):
        for x in range(minx, maxx +1):
            p = point2d(x, y)
            tile = tiles.get(p.__repr__())
            if tile is None or tile[1] == 0:
                output += " "
            else:
                output += "X"
        output += "\n"

    print(output)

    return



part2(intcode_computer(utils.input.getInputAsCSVInts()))
