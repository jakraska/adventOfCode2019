import utils.input
from utils.grid import HashGrid
from days.day11.intcode_computer import  intcode_computer
from typing import List


def parse_grid(code:List[int]) -> HashGrid:
    ic = intcode_computer(code)
    ic.execute([])
    g = HashGrid(" ")
    for i in range(0, len(ic.output), 3):
        g.set_value(ic.output[i],ic.output[i+1],ic.output[i+2])

    return g


def part1():
    game = parse_grid(utils.input.getInputAsCSVInts())

    blocks = filter(lambda x: x.value == 2 ,game.get_data())
    print(len(list(blocks)))

def move(ball_x, paddle_x):
    if ball_x == paddle_x:
        return 0
    return 1 if ball_x > paddle_x else -1

def part2():
    code = utils.input.getInputAsCSVInts()
    code[0] = 2
    ic = intcode_computer(code)

    omap = {
        '0': ' ',
        '1': 'X',
        '2': '#',
        '3': '=',
        '4': 'O',
    }

    ball_x = 0
    paddle_x = 0
    score = 0
    g = HashGrid(0)
    while not ic.is_complete:
        ic.execute([move(ball_x, paddle_x)])
        out = ic.pop_output()

        for i in range(0, len(out), 3):
            x, y, v = (out[i], out[i+1], out[i+2])
            if (x == -1 and y == 0):
                score = v
                continue
            elif v == 3:
                paddle_x = x
            elif v == 4:
                ball_x = x
            g.set_value(x, y, v)
        print(g.as_string(invert=True, output_map=omap))

    print(score)

part2()


