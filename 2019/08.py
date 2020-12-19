import util


def part1(data):
    width, height = 25, 6
    layers = len(data) // (width * height)

    result = (None, 0)

    for layer in range(layers):
        z = layer * width * height
        count = [0, 0, 0]

        for y in range(height):
            for x in range(width):
                count[data[z + (y * width) + x]] += 1

        if result[0] is None or count[0] < result[0]:
            result = (count[0], count[1] * count[2])

    return result[1]


def part2(nums):
    width, height = 25, 6
    layers = len(data) // (width * height)

    image = [[2 for x in range(width)] for y in range(height)]

    for layer in range(layers):
        z = layer * width * height

        for y in range(height):
            for x in range(width):
                if image[y][x] == 2:
                    image[y][x] = data[z + (y * width) + x]

    result = "\n"
    for y in range(height):
        for x in range(width):
            result += "O" if image[y][x] == 1 else "."
        result += "\n"

    return result[:-1]


line = util.read_line("input/08.txt")
data = [int(px) for px in line]
util.run(part1, part2, data)
