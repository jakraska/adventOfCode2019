import utils.input
from typing import List


def part1(start, end):
    n = [int(c) for c in start]
    max = [int(c) for c in end]

    valid_count = 0
    while within_max(n, max):
        if is_valid(n):
            valid_count += 1
        next_value(n)

    print(valid_count)


def part2(start, end):
    n = [int(c) for c in start]
    max = [int(c) for c in end]

    valid_count = 0
    while within_max(n, max):
        if is_valid(n) and is_valid_group(n):
            valid_count += 1
        next_value(n)

    print(valid_count)

def next_value(num:List[int]):
    s = 0
    for i in range(5, -1, -1):
        if num[i] != 9:
            num[i] += 1
            for j in range(i, 6):
                num[j] = num[i]
            break


def within_max(num:List[int], max:List[int]):
    for i in range(6):
        if num[i] < max[i]:
            return True
        elif num[i] > max[i]:
            return False
    return True


def is_valid(num:List[int]):
    dupe_found = False
    for i in range(5):
        if num[i] > num[i+1]:
            return False

        if num[i] == num[i+1]:
            dupe_found = True

    return dupe_found

def is_valid_group(num:List[int]):
    dupe_num = num[0]
    dupe_count = 1

    for i in range(1, len(num)):
        if num[i] == dupe_num:
            dupe_count += 1
        elif dupe_count == 2:
            return True
        else:
            dupe_count = 1
            dupe_num = num[i]

    return dupe_count == 2

input_str = utils.input.getInput().readline()
start = input_str[0:6]
end = input_str[7::]
part2(start, end)