import util

program = util.read_line("input/02.txt")
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

print(memory[0])
