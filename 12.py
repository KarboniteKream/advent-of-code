import math
import util


def rotate(x, y, angle):
    nx = x * math.cos(angle) - y * math.sin(angle)
    ny = x * math.sin(angle) + y * math.cos(angle)
    return nx, ny


def part1(commands):
    x, y = 0, 0
    angle = 0

    for command in commands:
        direction = command[0]
        amount = int(command[1:])

        if direction == "N":
            y += amount
        elif direction == "S":
            y -= amount
        elif direction == "E":
            x += amount
        elif direction == "W":
            x -= amount
        elif direction == "L":
            angle += math.radians(amount)
        elif direction == "R":
            angle -= math.radians(amount)
        elif direction == "F":
            x += amount * math.cos(angle)
            y += amount * math.sin(angle)

    return round(abs(x) + abs(y))


def part2(commands):
    sx, sy = 0, 0
    wx, wy = 10, 1

    for command in commands:
        direction = command[0]
        amount = int(command[1:])

        if direction == "N":
            wy += amount
        elif direction == "S":
            wy -= amount
        elif direction == "E":
            wx += amount
        elif direction == "W":
            wx -= amount
        elif direction == "L":
            angle = math.radians(amount)
            wx, wy = rotate(wx, wy, angle)
        elif direction == "R":
            angle = math.radians(amount)
            wx, wy = rotate(wx, wy, -angle)
        elif direction == "F":
            sx += amount * wx
            sy += amount * wy

    return round(abs(sx) + abs(sy))


commands = util.read_lines("input/12.txt")
util.run(part1, part2, commands)
