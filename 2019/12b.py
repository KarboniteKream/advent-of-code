import itertools
import math
import util


def parse_input(line):
    data = line[1:-1].split(", ")
    position = list(map(lambda x: int(x.split("=")[1]), data))
    velocity = [0, 0, 0]

    return [position, velocity]


def state(moons, axis):
    return [x[axis] for moon in moons for x in moon]


def calculate(moons, axis):
    steps = 0

    start = state(moons, axis)
    pairs = list(itertools.combinations(moons, 2))

    while True:
        if state(moons, axis) == start and steps > 0:
            return steps

        for (p1, v1), (p2, v2) in pairs:
            if p1[axis] < p2[axis]:
                v1[axis] += 1
                v2[axis] -= 1
            elif p1[axis] > p2[axis]:
                v1[axis] -= 1
                v2[axis] += 1

        for moon in moons:
            moon[0][axis] += moon[1][axis]

        steps += 1


moons = list(map(parse_input, util.read_lines("input/12.txt")))
result = 1

for axis in range(3):
    value = calculate(moons, axis)
    result = result * value // math.gcd(result, value)

print(result)
