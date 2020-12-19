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


filename = "input/03.txt"
first = get_lines(util.read_line(filename, 0).split(","))
second = get_lines(util.read_line(filename, 1).split(","))

result = None

for (s1, e1, d1) in first:
    for (s2, e2, d2) in second:
        if d1 == d2:
            continue

        (x1, y1), (x2, _) = (s1, e1) if d1 else (s2, e2)
        (x3, y3), (_, y4) = (s2, e2) if d1 else (s1, e1)

        if x1 < x3 and x3 < x2 and y3 < y1 and y1 < y4:
            dist = abs(x3) + abs(y1)

            if result is None or dist < result:
                result = dist

            continue

print(result)
