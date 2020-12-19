import util


def execute(memory):
    ptr = 0
    base = 0

    while ptr < len(memory):
        instruction = memory[ptr]

        opcode = instruction % 100
        modes = instruction // 100

        if opcode == 99:
            break

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
            memory[dst] = int(input("> "))
            ptr += 2
        elif opcode == 4:
            value = util.get_arg(memory, ptr, modes, 1, base)
            print(value)
            ptr += 2
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


program = util.read_line("input/09.txt")
memory = list(map(int, program.split(",")))
memory += [0] * 10000

execute(memory)
