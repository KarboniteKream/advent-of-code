import util


def get_lines(moves):
    lines = []
    start = (0, 0)

    for move in moves:
        direction = move[0]
        num = int(move[1:])

        if direction == "R":
            end = (start[0] + num, start[1])
        elif direction == "L":
            end = (start[0] - num, start[1])
        elif direction == "U":
            end = (start[0], start[1] + num)
        elif direction == "D":
            end = (start[0], start[1] - num)

        lines.append((start, end, direction in ["L", "R"]))
        start = end

    return lines


def get_points(moves):
    points = {}
    x, y = 0, 0
    cost = 0

    for move in moves:
        direction = move[0]
        num = int(move[1:])

        for _ in range(num):
            if direction == "R":
                x += 1
            elif direction == "L":
                x -= 1
            elif direction == "U":
                y += 1
            elif direction == "D":
                y -= 1

            cost += 1

            if (x, y) not in points:
                points[(x, y)] = cost

    return points


def part1(lines):
    line1 = get_lines(lines[0].split(","))
    line2 = get_lines(lines[1].split(","))

    result = None
    for (s1, e1, d1) in line1:
        for (s2, e2, d2) in line2:
            if d1 == d2:
                continue

            (x1, y1), (x2, _) = (s1, e1) if d1 else (s2, e2)
            (x3, y3), (_, y4) = (s2, e2) if d1 else (s1, e1)

            if x1 < x3 and x3 < x2 and y3 < y1 and y1 < y4:
                dist = abs(x3) + abs(y1)

                if result is None or dist < result:
                    result = dist

                continue

    return result


def part2(lines):
    line1 = get_points(lines[0].split(","))
    line2 = get_points(lines[1].split(","))

    intersection = set(line1.keys()) & set(line2.keys())
    return min(map(lambda p: line1[p] + line2[p], intersection))


lines = util.read_lines("input/03.txt")
util.run(part1, part2, lines)
