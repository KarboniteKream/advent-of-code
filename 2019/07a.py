import itertools
import util


def execute(memory, input):
    ptr = 0
    output = 0

    while ptr < len(memory):
        instruction = memory[ptr]

        opcode = instruction % 100
        modes = instruction // 100

        if opcode == 99:
            return output

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


program = util.read_line("input/07.txt")
permutations = itertools.permutations(range(5))
result = 0

for phases in permutations:
    output = 0

    for phase in phases:
        memory = list(map(int, program.split(",")))
        output = execute(memory, [phase, output])

    result = max(result, output)

print(result)
