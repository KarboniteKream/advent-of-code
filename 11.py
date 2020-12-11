import util


DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1),
]


def get_seat(layout, y, x):
    if 0 <= y < len(layout) and 0 <= x < len(layout[y]):
        return layout[y][x]

    return None


def count_occupied_adjacent(layout, y, x):
    count = 0

    for dy, dx in DIRECTIONS:
        seat = get_seat(layout, y + dy, x + dx)
        count += (seat == "#")

    return count


def count_occupied_direction(layout, y, x):
    count = 0

    for dy, dx in DIRECTIONS:
        for d in range(1, 100):
            seat = get_seat(layout, y + (d * dy), x + (d * dx))

            if seat != ".":
                count += (seat == "#")
                break

    return count


def run(layout, fn, limit):
    unstable = True

    while unstable:
        new_layout = [list(row) for row in layout]
        unstable = False

        for y in range(len(layout)):
            for x in range(len(layout[y])):
                if layout[y][x] == ".":
                    continue

                occupied = fn(layout, y, x)
                if layout[y][x] == "L" and occupied == 0:
                    new_layout[y][x] = "#"
                    unstable = True
                elif layout[y][x] == "#" and occupied >= limit:
                    new_layout[y][x] = "L"
                    unstable = True

        layout = new_layout

    return sum(seat == "#" for row in layout for seat in row)


def part1(layout):
    return run(layout, count_occupied_adjacent, 4)


def part2(layout):
    return run(layout, count_occupied_direction, 5)


lines = util.read_lines("input/11.txt")
layout = [list(line) for line in lines]
util.run(part1, part2, layout)
