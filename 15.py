import util


def speak(numbers, target):
    *spoken, last = numbers
    spoken = {num: idx for idx, num in enumerate(spoken)}

    for turn in range(len(numbers), target):
        if last not in spoken:
            curr = 0
        else:
            curr = turn - 1 - spoken[last]

        spoken[last] = turn - 1
        last = curr

    return last


def part1(numbers):
    return speak(numbers, 2020)


def part2(numbers):
    return speak(numbers, 30_000_000)


lines = util.read_lines("input/15.txt")
numbers = list(map(int, lines[0].split(",")))
util.run(part1, part2, numbers)
