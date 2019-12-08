import utils.input


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def part1():
    data = list(chunks(utils.input.getInputAsInts(), 25 * 6))
    min_zero_layer = min(data, key=lambda x: x.count(0))
    print(min_zero_layer.count(1) * min_zero_layer.count(2))

def part2():
    data = list(chunks(utils.input.getInputAsInts(), 25 * 6))

    final = []
    for i in range(25*6):
        val = 2
        for layer in data:
            if layer[i] != 2:
                val = layer[i]
                break
        final.append(val)

    output = ""
    for i in range(len(final)):
        if i % 25 == 0:
            output += "\n"
        output += str(final[i])
    print(output)



part2()