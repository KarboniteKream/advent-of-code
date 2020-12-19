import util


def execute(commands):
    ips = set()

    ip = 0
    acc = 0

    while ip < len(commands):
        if ip in ips:
            return False, acc

        ips.add(ip)
        op, n = commands[ip]
        step = 1

        if op == "acc":
            acc += n
        elif op == "jmp":
            step = n

        ip += step

    return True, acc


def part1(commands):
    _, acc = execute(commands)
    return acc


def part2(commands):
    for i in range(len(commands)):
        op, n = commands[i]
        new_op = op

        if op == "jmp":
            new_op = "nop"
        elif op == "nop":
            new_op = "jmp"

        commands[i] = (new_op, n)
        valid, acc = execute(commands)
        commands[i] = (op, n)

        if valid:
            break

    return acc


lines = util.read_lines("input/08.txt")

commands = []
for line in lines:
    op, n = line.split(" ")
    commands.append((op, int(n)))

util.run(part1, part2, commands)
