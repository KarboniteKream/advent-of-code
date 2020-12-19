import util


def execute(memory, input):
    ptr = 0
    result = 0

    while ptr < len(memory):
        instruction = memory[ptr]

        opcode = instruction % 100
        modes = instruction // 100

        if opcode == 99:
            break

        if opcode == 1:
            arg1 = util.get_arg(memory, ptr, modes, 1)
            arg2 = util.get_arg(memory, ptr, modes, 2)
            memory[memory[ptr + 3]] = arg1 + arg2
            ptr += 4
        elif opcode == 2:
            arg1 = util.get_arg(memory, ptr, modes, 1)
            arg2 = util.get_arg(memory, ptr, modes, 2)
            memory[memory[ptr + 3]] = arg1 * arg2
            ptr += 4
        elif opcode == 3:
            memory[memory[ptr + 1]] = input
            ptr += 2
        elif opcode == 4:
            result = util.get_arg(memory, ptr, modes, 1)
            ptr += 2
        elif opcode == 5:
            arg1 = util.get_arg(memory, ptr, modes, 1)
            arg2 = util.get_arg(memory, ptr, modes, 2)
            ptr = ptr + 3 if arg1 == 0 else arg2
        elif opcode == 6:
            arg1 = util.get_arg(memory, ptr, modes, 1)
            arg2 = util.get_arg(memory, ptr, modes, 2)
            ptr = arg2 if arg1 == 0 else ptr + 3
        elif opcode == 7:
            arg1 = util.get_arg(memory, ptr, modes, 1)
            arg2 = util.get_arg(memory, ptr, modes, 2)
            memory[memory[ptr + 3]] = int(arg1 < arg2)
            ptr += 4
        elif opcode == 8:
            arg1 = util.get_arg(memory, ptr, modes, 1)
            arg2 = util.get_arg(memory, ptr, modes, 2)
            memory[memory[ptr + 3]] = int(arg1 == arg2)
            ptr += 4

    return result


def part1(memory):
    memory = list(memory)
    return execute(memory, 1)


def part2(memory):
    memory = list(memory)
    return execute(memory, 5)


program = util.read_line("input/05.txt")
memory = list(map(int, program.split(",")))
util.run(part1, part2, memory)
