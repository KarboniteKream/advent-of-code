import util


def part1(input):
    seen = set()

    for num in input:
        other = 2020 - num
        if other in seen:
            return num * other

        seen.add(num)


def part2(input):
    seen = set(input)

    for i, num1 in enumerate(input):
        for num2 in input[i + 1:]:
            other = 2020 - num1 - num2
            if other in seen:
                return num1 * num2 * other


input = util.read_lines("input/01.txt", int)
util.run(input, part1, part2)
