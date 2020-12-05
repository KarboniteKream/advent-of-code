import util


def is_valid_old(line):
    cnt, char, password = line.split(" ")
    min, max = list(map(int, cnt.split("-")))
    char = char[0]

    num = password.count(char)
    return min <= num and num <= max


def is_valid_new(line):
    cnt, char, password = line.split(" ")
    i, j = list(map(int, cnt.split("-")))
    char = char[0]

    p1 = password[i - 1]
    p2 = password[j - 1]

    return p1 != p2 and (p1 == char or p2 == char)


def part1(input):
    return len(list(filter(is_valid_old, input)))


def part2(input):
    return len(list(filter(is_valid_new, input)))


input = util.read_lines("input/02.txt", str)
util.run(input, part1, part2)