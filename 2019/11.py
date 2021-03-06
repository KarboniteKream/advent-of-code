import util


def execute(state, input):
    memory, ptr, base = state
    output = []

    while ptr < len(memory):
        instruction = memory[ptr]

        opcode = instruction % 100
        modes = instruction // 100

        if opcode == 99:
            state[:] = memory, ptr, base
            return (output, True)

        if opcode == 1:
            arg1 = util.get_arg(memory, ptr, modes, 1, base)
            arg2 = util.get_arg(memory, ptr, modes, 2, base)
            arg3 = util.get_arg(memory, ptr, modes, 3, base, True)
            memory[arg3] = arg1 + arg2
            ptr += 4
        elif opcode == 2:
            arg1 = util.get_arg(memory, ptr, modes, 1, base)
            arg2 = util.get_arg(memory, ptr, modes, 2, base)
            arg3 = util.get_arg(memory, ptr, modes, 3, base, True)
            memory[arg3] = arg1 * arg2
            ptr += 4
        elif opcode == 3:
            dst = util.get_arg(memory, ptr, modes, 1, base, True)
            memory[dst] = input
            ptr += 2
        elif opcode == 4:
            value = util.get_arg(memory, ptr, modes, 1, base)
            output.append(value)
            ptr += 2

            if len(output) == 2:
                state[:] = memory, ptr, base
                return (output, False)
        elif opcode == 5:
            arg1 = util.get_arg(memory, ptr, modes, 1, base)
            arg2 = util.get_arg(memory, ptr, modes, 2, base)
            ptr = ptr + 3 if arg1 == 0 else arg2
        elif opcode == 6:
            arg1 = util.get_arg(memory, ptr, modes, 1, base)
            arg2 = util.get_arg(memory, ptr, modes, 2, base)
            ptr = arg2 if arg1 == 0 else ptr + 3
        elif opcode == 7:
            arg1 = util.get_arg(memory, ptr, modes, 1, base)
            arg2 = util.get_arg(memory, ptr, modes, 2, base)
            arg3 = util.get_arg(memory, ptr, modes, 3, base, True)
            memory[arg3] = int(arg1 < arg2)
            ptr += 4
        elif opcode == 8:
            arg1 = util.get_arg(memory, ptr, modes, 1, base)
            arg2 = util.get_arg(memory, ptr, modes, 2, base)
            arg3 = util.get_arg(memory, ptr, modes, 3, base, True)
            memory[arg3] = int(arg1 == arg2)
            ptr += 4
        elif opcode == 9:
            base += util.get_arg(memory, ptr, modes, 1, base)
            ptr += 2


def part1(memory):
    state = [list(memory), 0, 0]

    panels = {}
    position = (0, 0)
    delta = (0, 1)
    result = 0

    while True:
        color = panels.get(position, 0)
        output, done = execute(state, color)

        if done:
            break

        if position not in panels:
            result += 1

        panels[position] = output[0]

        if delta == (0, 1):
            delta = (-1, 0) if output[1] == 0 else (1, 0)
        elif delta == (0, -1):
            delta = (1, 0) if output[1] == 0 else (-1, 0)
        elif delta == (-1, 0):
            delta = (0, -1) if output[1] == 0 else (0, 1)
        elif delta == (1, 0):
            delta = (0, 1) if output[1] == 0 else (0, -1)

        position = (position[0] + delta[0], position[1] + delta[1])

    return result


def part2(memory):
    state = [list(memory), 0, 0]

    panels = {}
    position = (0, 0)
    delta = (0, 1)
    panels[position] = 1

    while True:
        color = panels.get(position, 0)
        output, done = execute(state, color)

        if done:
            break

        panels[position] = output[0]

        if delta == (0, 1):
            delta = (-1, 0) if output[1] == 0 else (1, 0)
        elif delta == (0, -1):
            delta = (1, 0) if output[1] == 0 else (-1, 0)
        elif delta == (-1, 0):
            delta = (0, -1) if output[1] == 0 else (0, 1)
        elif delta == (1, 0):
            delta = (0, 1) if output[1] == 0 else (0, -1)

        position = (position[0] + delta[0], position[1] + delta[1])

    points = [k for k, v in panels.items() if v == 1]

    sx, sy = points[0]
    ex, ey = points[0]

    for x, y in points:
        sx = min(sx, x)
        sy = min(sy, y)
        ex = max(ex, x)
        ey = max(ey, y)

    width = ex - sx + 1
    height = ey - sy + 1
    image = [[0 for x in range(width)] for y in range(height)]

    for x, y in points:
        image[height - y + sy - 1][x - sx] = 1

    result = "\n"
    for y in range(height):
        for x in range(width):
            result += "O" if image[y][x] == 1 else "."
        result += "\n"

    return result[:-1]


program = util.read_line("input/11.txt")
memory = list(map(int, program.split(",")))
memory += [0] * 10000
util.run(part1, part2, memory)
