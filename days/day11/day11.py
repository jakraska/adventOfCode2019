import utils.input
import math
from utils.grid import point2d, HashGrid
from days.day11.intcode_computer import intcode_computer


def rotate(vector:point2d, turn:int):
    angle = (math.pi / 2) if turn == 0 else -1 *(math.pi / 2)
    sin = int(math.sin(angle))
    cos = int(math.cos(angle))
    return point2d(vector.x * cos - vector.y * sin, vector.y * cos + vector.x * sin )

def part1(computer:intcode_computer):
    pos = point2d(0,0)
    forward = point2d(0,1)
    grid = HashGrid(0)

    while not computer.is_complete:
        curr_color = grid.get_value(pos.x, pos.y)
        computer.execute([curr_color])
        grid.set_value(pos.x, pos.y, computer.output.pop(0))
        turn = computer.output.pop(0)
        forward = rotate(forward, turn)
        pos.x += forward.x
        pos.y += forward.y

    print(len(grid.data))
    return


def part2(computer:intcode_computer):
    pos = point2d(0, 0)
    forward = point2d(0, 1)
    grid = HashGrid(0)
    grid.set_value(pos.x, pos.y, 1)

    while not computer.is_complete:
        curr_color = grid.get_value(pos.x, pos.y)
        computer.execute([curr_color])
        grid.set_value(pos.x, pos.y, computer.output.pop(0))
        turn = computer.output.pop(0)
        forward = rotate(forward, turn)
        pos.x += forward.x
        pos.y += forward.y

    output = grid.as_string(output_map={"1":"X"})
    print(output)

    return


part2(intcode_computer(utils.input.getInputAsCSVInts()))
