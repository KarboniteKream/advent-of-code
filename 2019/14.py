import math
import util


def calculate(formulas, amount):
    result = 0

    chemicals = {"FUEL": amount}
    extra = {}

    while chemicals:
        next = {}

        for chemical, amount in chemicals.items():
            inputs, output = formulas[chemical]

            needed = max(amount - extra.get(chemical, 0), 0)
            multiplier = math.ceil(needed / output)

            excess = output * multiplier - amount
            extra[chemical] = extra.get(chemical, 0) + excess

            for chemical, amount in inputs:
                count = amount * multiplier

                if chemical == "ORE":
                    result += count
                else:
                    next[chemical] = next.get(chemical, 0) + count

        chemicals = next

    return result


def part1(formulas):
    return calculate(formulas, 1)


def part2(formulas):
    result = calculate(formulas, 1)
    target = 1_000_000_000_000
    low = target // result
    high = 2 * low

    while low < high:
        mid = (low + high) // 2
        amount = calculate(formulas, mid)

        if amount > target:
            high = mid - 1
        else:
            result = mid
            low = mid + 1

    return result


lines = util.read_lines("input/14.txt")
formulas = {}

for line in lines:
    left, right = line.split(" => ")

    inputs = []
    for data in left.split(", "):
        amount, chemical = data.split(" ")
        inputs.append((chemical, int(amount)))

    amount, chemical = right.split(" ")
    formulas[chemical] = (inputs, int(amount))

util.run(part1, part2, formulas)
