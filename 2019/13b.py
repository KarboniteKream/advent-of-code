import util


def execute(state, screen):
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
                [x, y, value] = block
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


def render(screen):
    blocks = [" ", "|", "x", "-", "O"]

    for y in range(len(screen)):
        for x in range(len(screen[y])):
            print(blocks[screen[y][x]], end="")

        print()


program = util.read_line("input/13.txt")
memory = list(map(int, program.split(",")))
memory += [0] * 10000
memory[0] = 2

state = [memory, 0, 0]
screen = [[0 for x in range(38)] for y in range(21)]
result = execute(state, screen)

print(result)
