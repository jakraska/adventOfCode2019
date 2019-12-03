import utils.input


def part1():
    print(run_program(utils.input.getInputAsCSVInts(), 12, 2))


def part2():
    for i in range(100):
        for j in range(100):
            codes = utils.input.getInputAsCSVInts()
            if run_program(codes, i, j) == 19690720:
                print("success")
                print(100 * i + j)
                return


def run_program(codes, noun, verb):
    i = 0
    codes[1] = noun
    codes[2] = verb
    while codes[i] != 99:
        a = codes[codes[i + 1]]
        b = codes[codes[i + 2]]
        newVal = (a + b) if codes[i] == 1 else (a * b)
        codes[codes[i + 3]] = newVal
        i += 4
    return codes[0]


part2()

#part1()