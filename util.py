def read_lines(filename, fn=str):
    with open(filename) as file:
        return list(map(fn, file.read().splitlines()))


def run(input, part1, part2):
    print(part1(input))
    print(part2(input))
