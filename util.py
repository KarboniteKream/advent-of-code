def read(filename):
    with open(filename) as file:
        return file.read()


def read_lines(filename, fn=str):
    with open(filename) as file:
        return list(map(fn, file.read().splitlines()))


def run(part1, part2, *args):
    print("Part 1:", part1(*args))
    print("Part 2:", part2(*args))
