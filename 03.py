import util


def traverse(forest, dy, dx):
    w = len(forest[0])
    h = len(forest)
    y, x = 0, 0
    trees = 0

    while True:
        if forest[y][x] == "#":
            trees += 1

        y += dy
        x = (x + dx) % w

        if y >= h:
            break

    return trees


def part1(forest):
    return traverse(forest, 1, 3)


def part2(forest):
    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    trees = list(map(lambda slope: traverse(forest, *slope), slopes))

    result = 1
    for tree in trees:
        result *= tree
    return result


lines = util.read_lines("input/03.txt")
forest = [[x for x in line] for line in lines]
util.run(part1, part2, forest)
