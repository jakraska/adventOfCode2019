import utils.input
from typing import List


class action:
    def __init__(self, opt_code, param_modes, params):
        self.opt_code = opt_code
        self.param_modes = param_modes
        self.params = params

    def get_input_length(self):
        return len(self.params) + 1

    def execute(self, codes:List[int], user_input:List[int]):


        if self.opt_code == 1:
            val = self.get_param(0, codes) + self.get_param(1, codes)
            self.write_param(val, 2, codes)
        elif self.opt_code == 2:
            val = self.get_param(0, codes) * self.get_param(1, codes)
            self.write_param(val, 2, codes)
        elif self.opt_code == 3:
            val = user_input.pop(0)
            self.write_param(val, 0, codes)
        elif self.opt_code == 4:
            return self.get_param(0, codes)

        elif self.opt_code == 7:
            val = 1 if self.get_param(0, codes) < self.get_param(1, codes) else 0
            self.write_param(val, 2, codes)

        elif self.opt_code == 8:
            val = 1 if self.get_param(0, codes) == self.get_param(1, codes) else 0
            self.write_param(val, 2, codes)


    def is_end(self):
        return self.opt_code == 99

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


def run_program(codes, user_input: List[int]):
    i = 0
    a = next_action(codes, i)
    output = None
    while not a.is_end():
        output = a.execute(codes, user_input)
        i = a.next_index(codes, i)
        a = next_action(codes, i)
    return output


def get_all_combos(init_list: List[int]):
    if len(init_list) == 1:
        return [[init_list[0]]]
    output = []
    for i in init_list:
        new_list = init_list.copy()
        new_list.remove(i)

        for x in get_all_combos(new_list):
            x.append(i)
            output.append(x)

    return output


class amp:
    def __init__(self, phase_setting:int, program:List[int]):
        self.phase_setting = phase_setting
        self.program = program
        self.is_complete = False
        self.index = 0
        self.input = [phase_setting]
        self.next_amp = None
        self.output = []

    def execute(self):
        a = next_action(self.program, self.index)

        while not a.is_end() and not (a.opt_code == 3 and len(self.input) == 0):
            output = a.execute(self.program, self.input)
            if output is not None:
                self.next_amp.input.append(output)
                self.output.append(output)
            self.index = a.next_index(self.program, self.index)
            a = next_action(self.program, self.index)

        if a.is_end():
            self.is_complete = True


def part1():
    max_val = None
    for ps_list in get_all_combos([0,1,2,3,4]):
        last_output = 0
        for ps in ps_list:
            last_output = run_program(utils.input.getInputAsCSVInts(), [ps, last_output])
        max_val = last_output if max_val is None else max(max_val, last_output)
    print(max_val)


def part2():
    max_val = None
    all_ps = get_all_combos([5, 6, 7, 8, 9])
    for ps_list in all_ps:
        amps = []
        for ps in ps_list:
            amps.append(amp(ps, utils.input.getInputAsCSVInts()))
        amps[0].input.append(0)
        for i in range(len(amps) - 1):
            amps[i].next_amp = amps[i+1]
        amps[-1].next_amp = amps[0]

        a = amps[0]
        while not a.is_complete:
            a.execute()
            a = a.next_amp

        output = amps[-1].output[-1]
        max_val = output if max_val is None else max(max_val, output)
    print(max_val)


part2()