import math
import util

lines = util.read_lines("input/14.txt")
formulas = {}

for line in lines:
    [left, right] = line.split(" => ")
    inputs = []

    for data  in left.split(", "):
        [amount, chemical] = data.split(" ")
        inputs.append((chemical, int(amount)))

    [amount, chemical] = right.split(" ")
    formulas[chemical] = (inputs, int(amount))

result = 0
chemicals = {"FUEL": 1}
extra = {}

while True:
    if not chemicals:
        break

    next = {}

    for chemical, amount in chemicals.items():
        (inputs, output) = formulas[chemical]

        needed = max(amount - extra.get(chemical, 0), 0)
        multiplier = math.ceil(needed / output)

        excess = output * multiplier - amount
        extra[chemical] = extra.get(chemical, 0) + excess

        for (chemical, amount) in inputs:
            count = amount * multiplier

            if chemical == "ORE":
                result += count
            else:
                next[chemical] = next.get(chemical, 0) + count

    chemicals = next

print(result)
