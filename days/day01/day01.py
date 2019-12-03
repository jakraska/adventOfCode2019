import utils.input


def part1(input):
    total_sum = 0
    for x in input:
        total_sum += int(x / 3) - 2

    print(total_sum)


def part2(input):
    total_sum = 0
    for x in input:
        fuel = calc_fuel(x)

        while fuel > 0:
            total_sum += fuel
            fuel = calc_fuel(fuel)
    print(total_sum)


def calc_fuel(mass:int):
    return int(mass / 3) - 2




#part1(utils.input.getInputAsInts())

part2(utils.input.getInputAsInts())




