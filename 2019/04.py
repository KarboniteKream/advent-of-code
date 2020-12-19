import util


def part1(low, high):
    def is_valid(number):
        digits = str(number)
        valid = False

        for i in range(5):
            if digits[i] > digits[i + 1]:
                return False

            if digits[i] == digits[i + 1]:
                valid = True

        return valid

    return sum(is_valid(num) for num in range(low, high + 1))


def part2(low, high):
    def is_valid(number):
        digits = str(number)
        count = [0] * 10
        count[int(digits[5])] = 1

        for i in range(5):
            if digits[i] > digits[i + 1]:
                return False

            count[int(digits[i])] += 1

        return 2 in count

    return sum(is_valid(num) for num in range(low, high + 1))


low, high = map(int, util.read_line("input/04.txt").split("-"))
util.run(part1, part2, low, high)
