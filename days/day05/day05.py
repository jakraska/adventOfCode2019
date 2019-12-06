import utils.input
from typing import List

user_input = None

class action:
    def __init__(self, opt_code, param_modes, params):
        self.opt_code = opt_code
        self.param_modes = param_modes
        self.params = params

    def get_input_length(self):
        return len(self.params) + 1

    def execute(self, codes:List[int]):
        if self.opt_code == 99:
            print("complete")
            return True

        if self.opt_code == 1:
            val = self.get_param(0, codes) + self.get_param(1, codes)
            self.write_param(val, 2, codes)
        elif self.opt_code == 2:
            val = self.get_param(0, codes) * self.get_param(1, codes)
            self.write_param(val, 2, codes)
        elif self.opt_code == 3:
            val = user_input
            self.write_param(val, 0, codes)
        elif self.opt_code == 4:
            print(self.get_param(0, codes))

        elif self.opt_code == 7:
            val = 1 if self.get_param(0, codes) < self.get_param(1, codes) else 0
            self.write_param(val, 2, codes)

        elif self.opt_code == 8:
            val = 1 if self.get_param(0, codes) == self.get_param(1, codes) else 0
            self.write_param(val, 2, codes)

        return False

    def get_param(self, pram_num:int, codes:List[int]):
        return codes[self.params[pram_num]] if self.param_modes[pram_num] == 0 else self.params[pram_num]

    def write_param(self, val:int, pram_num:int, codes:List[int]):
        codes[self.params[pram_num]] = val

    def next_index(self, codes:List[int], current_index:int):
        if (self.opt_code == 5 and self.get_param(0, codes) != 0) or (self.opt_code == 6 and self.get_param(0, codes) == 0) :
            return self.get_param(1, codes)

        return self.get_input_length() + current_index


def next_action(codes:List[int], start:int) -> action:
    opt_code = int(str(codes[start])[-2:])
    param_modes = [int(c) for c in str(codes[start])[0:-2][::-1]]
    param_len = 0
    if opt_code == 1 or opt_code == 2 or opt_code == 7 or opt_code == 8:
        param_len = 3
    elif opt_code == 3 or opt_code == 4:
        param_len = 1
    elif opt_code == 5 or opt_code == 6:
        param_len = 2

    while len(param_modes) < param_len:
        param_modes.append(0)

    params = []
    for i in range(param_len):
        params.append(codes[start + i + 1])

    return action(opt_code, param_modes, params)

def run_program(codes):
    i = 0
    a = next_action(codes, i)
    while not a.execute(codes):
        i = a.next_index(codes, i)
        a = next_action(codes, i)

def part1():
    global user_input
    user_input = 1
    run_program(utils.input.getInputAsCSVInts())


def part2():
    global user_input
    user_input = 5
    run_program(utils.input.getInputAsCSVInts())


part2()