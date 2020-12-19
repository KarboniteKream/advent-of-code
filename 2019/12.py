import itertools
import math
import util


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


def part1(moons):
    for _ in range(1000):
        for a in range(len(moons)):
            for b in range(a, len(moons)):
                if a == b:
                    continue

                for axis in range(3):
                    if moons[a][0][axis] < moons[b][0][axis]:
                        moons[a][1][axis] += 1
                        moons[b][1][axis] -= 1
                    elif moons[a][0][axis] > moons[b][0][axis]:
                        moons[a][1][axis] -= 1
                        moons[b][1][axis] += 1

        for moon in moons:
            for axis in range(3):
                moon[0][axis] += moon[1][axis]

    result = 0

    for moon in moons:
        result += sum(map(abs, moon[0])) * sum(map(abs, moon[1]))

    return result


def part2(moons):
    result = 1

    for axis in range(3):
        value = calculate(moons, axis)
        result = result * value // math.gcd(result, value)

    return result


lines = util.read_lines("input/12.txt")
moons = []

for line in lines:
    data = line[1:-1].split(", ")
    position = [int(x.split("=")[1]) for x in data]
    velocity = [0, 0, 0]
    moons.append((position, velocity))

util.run(part1, part2, moons)
