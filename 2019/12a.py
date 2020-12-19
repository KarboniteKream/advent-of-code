import util


def parse_input(line):
    data = line[1:-1].split(", ")
    position = list(map(lambda x: int(x.split("=")[1]), data))
    velocity = [0, 0, 0]

    return [position, velocity]


moons = list(map(parse_input, util.read_lines("input/12.txt")))

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

print(result)
