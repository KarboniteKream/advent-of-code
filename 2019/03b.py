import util


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


filename = "input/03.txt"
first = get_points(util.read_line(filename, 0).split(","))
second = get_points(util.read_line(filename, 1).split(","))

intersection = set(first.keys()) & set(second.keys())
result = min(map(lambda p: first[p] + second[p], intersection))

print(result)
