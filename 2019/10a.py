import math
import util

data = util.read_lines("input/10.txt")
asteroids = []

for y, row in enumerate(data):
    for x, column in enumerate(row):
        if column == "#":
            asteroids.append((x, y))

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

print(result)
