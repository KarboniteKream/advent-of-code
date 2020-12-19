import util


def execute(memory, noun, verb):
    memory[1] = noun
    memory[2] = verb

    for i in range(0, len(memory), 4):
        opcode = memory[i]

        if opcode == 99:
            break

        arg1 = memory[memory[i + 1]]
        arg2 = memory[memory[i + 2]]
        dst = memory[i + 3]

        memory[dst] = arg1 + arg2 if opcode == 1 else arg1 * arg2

    return memory[0]


def part1(program):
    memory = list(map(int, program.split(",")))

    memory[1] = 12
    memory[2] = 2

    for i in range(0, len(memory), 4):
        opcode = memory[i]

        if opcode == 99:
            break

        p1 = memory[memory[i + 1]]
        p2 = memory[memory[i + 2]]
        dst = memory[i + 3]

        memory[dst] = p1 + p2 if opcode == 1 else p1 * p2

    return memory[0]


def part2(program):
    expected = 19690720

    for noun in range(100):
        for verb in range(100):
            memory = list(map(int, program.split(",")))
            result = execute(memory, noun, verb)

            if result == expected:
                return 100 * noun + verb


program = util.read_line("input/02.txt")
util.run(part1, part2, program)
