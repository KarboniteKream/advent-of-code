import util


def part1(modules):
    fuel = 0

    for mass in modules:
        fuel += mass // 3 - 2

    return fuel


def part2(modules):
    fuel = 0

    for mass in modules:
        while mass > 0:
            mass = max(mass // 3 - 2, 0)
            fuel += mass

    return fuel


modules = util.read_lines("input/01.txt", int)
util.run(part1, part2, modules)
