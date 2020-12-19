def run(part1, part2, *args):
    print("Part 1:", part1(*args))
    print("Part 2:", part2(*args))


def read_lines(filename, fn=str):
    with open(filename) as file:
        return list(map(fn, file.read().splitlines()))


def read_line(filename, idx=0):
    with open(filename) as file:
        return file.read().splitlines()[idx]


def get_arg(memory, ptr, modes, i, base=0, write=False):
    mode = (modes // 10 ** (i - 1)) % 10
    value = memory[ptr + i]

    if mode == 0:
        if write:
            return value
        else:
            return memory[value]

    if mode == 1:
        return value

    if mode == 2:
        if write:
            return base + value
        else:
            return memory[base + value]

    return None
