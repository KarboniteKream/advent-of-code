import collections
import itertools
import util


def get_deltas(dimensions):
    return list(itertools.product([-1, 0, 1], repeat=dimensions))


def run(cubes, dimensions):
    deltas = get_deltas(dimensions)

    for _ in range(6):
        active = collections.defaultdict(int)

        for cube in cubes:
            for delta in deltas:
                c = tuple(map(lambda x, y: x + y, cube, delta))
                active[c] += (c != cube)

        new_cubes = set()
        for cube, neighbours in active.items():
            if cube in cubes and neighbours in [2, 3]:
                new_cubes.add(cube)
            elif cube not in cubes and neighbours == 3:
                new_cubes.add(cube)

        cubes = new_cubes

    return len(cubes)


def part1(cubes):
    cubes = {(0, *cube) for cube in cubes}
    return run(cubes, 3)


def part2(cubes):
    cubes = {(0, 0, *cube) for cube in cubes}
    return run(cubes, 4)


lines = util.read_lines("input/17.txt")

cubes = set()
for y, line in enumerate(lines):
    for x, cube in enumerate(line):
        if cube == "#":
            cubes.add((y, x))

util.run(part1, part2, cubes)
