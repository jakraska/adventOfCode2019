import utils.input
from typing import List

class action:
    def __init__(self, opt_code, param_modes, params, rel_base):
        self.opt_code = opt_code
        self.param_modes = param_modes
        self.params = params
        self.rel_base = rel_base

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
        elif self.opt_code == 9:
            self.rel_base += self.get_param(0, codes)

    def is_end(self):
        return self.opt_code == 99

    def get_param(self, pram_num:int, codes:List[int]):
        if self.param_modes[pram_num] == 1:
            return self.params[pram_num]

        idx = None
        if self.param_modes[pram_num] == 0:
            idx = self.params[pram_num]
        elif self.param_modes[pram_num] == 2:
            idx = self.rel_base + self.params[pram_num]

        if idx > len(codes) - 1:
            return 0
        return codes[idx]

    def write_param(self, val:int, pram_num:int, codes:List[int]):
        idx = None
        if self.param_modes[pram_num] == 0:
            idx = self.params[pram_num]
        elif self.param_modes[pram_num] == 2:
            idx = self.rel_base + self.params[pram_num]

        while idx > len(codes) - 1:
            codes.append(0)

        codes[idx] = val

    def next_index(self, codes:List[int], current_index:int):
        if (self.opt_code == 5 and self.get_param(0, codes) != 0) or (self.opt_code == 6 and self.get_param(0, codes) == 0) :
            return self.get_param(1, codes)

        return self.get_input_length() + current_index


class intcode_computer:
    def __init__(self, program:List[int]):
        self.program = program
        self.is_complete = False
        self.index = 0
        self.rel_base = 0
        self.output = []

    def execute(self, user_input:List[int]):
        a = self.next_action(self.index, self.rel_base)

        while not a.is_end() and not (a.opt_code == 3 and len(user_input) == 0):
            output = a.execute(self.program, user_input)
            if output is not None:
                self.output.append(output)
            self.index = a.next_index(self.program, self.index)
            self.rel_base = a.rel_base
            a = self.next_action(self.index, self.rel_base)

        if a.is_end():
            self.is_complete = True

    def next_action(self, start: int, rel_base: int) -> action:
        opt_code = int(str(self.program[start])[-2:])
        param_modes = [int(c) for c in str(self.program[start])[0:-2][::-1]]
        param_len = 0
        if opt_code == 1 or opt_code == 2 or opt_code == 7 or opt_code == 8:
            param_len = 3
        elif opt_code == 3 or opt_code == 4 or opt_code == 9:
            param_len = 1
        elif opt_code == 5 or opt_code == 6:
            param_len = 2

        while len(param_modes) < param_len:
            param_modes.append(0)

        params = []
        for i in range(param_len):
            params.append(self.program[start + i + 1])

        return action(opt_code, param_modes, params, rel_base)