import itertools
import util


def execute(state, input):
    memory, ptr, output = state

    while ptr < len(memory):
        instruction = memory[ptr]

        opcode = instruction % 100
        modes = instruction // 100

        if opcode == 99:
            state[:] = memory, ptr, output
            return (output, True)

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
            memory[memory[ptr + 1]] = input.pop(0)
            ptr += 2
        elif opcode == 4:
            output = util.get_arg(memory, ptr, modes, 1)
            ptr += 2
            state[:] = memory, ptr, output
            return (output, False)
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


def part1(memory):
    result = 0

    for phases in itertools.permutations(range(5)):
        output = 0

        for phase in phases:
            state = [list(memory), 0, 0]
            output, _ = execute(state, [phase, output])

        result = max(result, output)

    return result


def part2(program):
    result = 0

    for phases in itertools.permutations(range(5, 10)):
        states = [
            [list(memory), 0, 0],
            [list(memory), 0, 0],
            [list(memory), 0, 0],
            [list(memory), 0, 0],
            [list(memory), 0, 0],
        ]

        inputs = [[phase] for phase in phases]
        output = 0
        done = False

        while done is False:
            for i in range(5):
                inputs[i].append(output)
                output, done = execute(states[i], inputs[i])

        result = max(result, output)

    return result


program = util.read_line("input/07.txt")
memory = list(map(int, program.split(",")))
util.run(part1, part2, memory)
