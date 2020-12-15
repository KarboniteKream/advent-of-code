import re
import util


def part1(lines):
    memory = {}
    mask0, mask1 = 0, 0

    for line in lines:
        if match := re.match(r"^mask = ([X01]+)$", line):
            mask, = match.groups()
            mask0 = int(mask.replace("X", "1"), 2)
            mask1 = int(mask.replace("X", "0"), 2)
        elif match := re.match(r"^mem\[(\d+)\] = (\d+)$", line):
            address, value = map(int, match.groups())
            memory[address] = (value & mask0) | mask1

    return sum(memory.values())


def part2(lines):
    memory = {}
    mask1 = 0
    floats = []

    for line in lines:
        if match := re.match(r"^mask = ([X01]+)$", line):
            mask, = match.groups()
            mask1 = int(mask.replace("X", "0"), 2)
            floats = [idx for idx, bit in enumerate(reversed(mask)) if bit == "X"]
        elif match := re.match(r"^mem\[(\d+)\] = (\d+)$", line):
            address, value = map(int, match.groups())

            for bits in range(2 ** len(floats)):
                for i, idx in enumerate(floats):
                    if (bits >> i) & 1:
                        address |= (1 << idx)
                    else:
                        address &= ~(1 << idx)

                memory[address | mask1] = value

    return sum(memory.values())


lines = util.read_lines("input/14.txt")
util.run(part1, part2, lines)
