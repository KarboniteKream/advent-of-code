import math
import util


def part1(asteroids):
    result = 0

    for a in asteroids:
        current = 0
        angles = set()

        for b in asteroids:
            if a == b:
                continue

            angle = math.atan2(b[1] - a[1], b[0] - a[0])

            if angle not in angles:
                angles.add(angle)
                current += 1

        result = max(result, current)

    return result


def part2(asteroids):
    best = 0
    scanner = None

    for a in asteroids:
        current = 0
        angles = set()

        for b in asteroids:
            if a == b:
                continue

            angle = math.atan2(b[1] - a[1], b[0] - a[0])

            if angle not in angles:
                angles.add(angle)
                current += 1

        if current > best:
            best = current
            scanner = a

    angles = {}
    order = []

    for a in asteroids:
        if a == scanner:
            continue

        dx, dy = a[0] - scanner[0], a[1] - scanner[1]
        angle = -(math.atan2(dx, dy) - (2 * math.pi))
        distance = math.sqrt(dx ** 2 + dy ** 2)

        if angle in angles:
            angles[angle].append((a, distance))
        else:
            angles[angle] = [(a, distance)]

    for angle in sorted(angles.keys()):
        data = sorted(angles[angle], key=lambda x: x[1], reverse=True)
        order.append(list(map(lambda x: x[0], data)))

    result = None
    count, idx = 0, 0

    while count < 200:
        idx %= len(order)

        if len(order[idx]) == 0:
            order.pop(idx)
            continue

        asteroid = order[idx].pop()
        result = asteroid[0] * 100 + asteroid[1]

        count += 1
        idx += 1

    return result


data = util.read_lines("input/10.txt")
asteroids = []

for y, row in enumerate(data):
    for x, column in enumerate(row):
        if column == "#":
            asteroids.append((x, y))

util.run(part1, part2, asteroids)
