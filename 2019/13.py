import util


def execute(state, screen, objects=[]):
    memory, ptr, base = state
    block = []

    score = 0
    paddle = 0
    ball = 0

    while ptr < len(memory):
        instruction = memory[ptr]

        opcode = instruction % 100
        modes = instruction // 100

        if opcode == 99:
            return score

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
            memory[dst] = (ball > paddle) - (ball < paddle)
            ptr += 2
        elif opcode == 4:
            value = util.get_arg(memory, ptr, modes, 1, base)
            block.append(value)
            ptr += 2

            if len(block) == 3:
                x, y, value = block
                objects.append((x, y, value))
                block = []

                if x >= 0 and y >= 0:
                    screen[y][x] = value
                else:
                    score = value

                if value == 3:
                    paddle = x
                elif value == 4:
                    ball = x
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


def part1(memory, screen):
    state = [list(memory), 0, 0]
    objects = []
    execute(state, screen, objects)

    result = 0
    for _, _, type in objects:
        if type == 2:
            result += 1

    return result


def part2(memory, screen):
    memory = list(memory)
    memory[0] = 2
    state = [memory, 0, 0]
    return execute(state, screen)


program = util.read_line("input/13.txt")
memory = list(map(int, program.split(",")))
memory += [0] * 10000
screen = [[0 for x in range(38)] for y in range(21)]
util.run(part1, part2, memory, screen)
