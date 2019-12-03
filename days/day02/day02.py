import utils.input


def part1(codes):
    codes[1] = 12
    codes[2] = 2
    run_program(codes)
    print(codes[0])


def part2():

    for i in range(100):
        for j in range(100):
            codes = utils.input.getInputAsCSVInts()
            codes[1] = i
            codes[2] = j
            run_program(codes)
            if codes[0] == 19690720:
                print("success")
                print(100 * i + j)
                return

def run_program(codes):
    i = 0
    while codes[i] != 99:
        a = codes[codes[i + 1]]
        b = codes[codes[i + 2]]
        newVal = (a + b) if codes[i] == 1 else (a * b)
        codes[codes[i + 3]] = newVal
        i += 4
    return codes

# def part2(input):


# codes = utils.input.getInputAsCSVInts()
# part1(codes)

part2()


#part1(utils.input.getInputAsInts())