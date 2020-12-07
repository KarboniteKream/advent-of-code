import util


def part1(input):
    data = {}

    for name, bags in input.items():
        for bag, _ in bags:
            data.setdefault(bag, []).append(name)

    result = set()
    bags = {"shiny gold"}

    while bags:
        bags = {b for bag in bags for b in data.get(bag, [])}
        result |= bags

    return len(result)


def part2(input):
    result = {}

    while input:
        new_input = {}

        for name, bags in input.items():
            total = 0
            ok = True

            for bag, count in bags:
                if bag not in result:
                    ok = False
                    break

                total += count * (1 + result[bag])

            if ok:
                result[name] = total
            else:
                new_input[name] = bags

        input = new_input

    return result["shiny gold"]


rules = util.read_lines("input/07.txt")
input = {}

for rule in rules:
    left, right = rule.split(" contain ")

    bags = []
    for bag in right.split(", "):
        count, *name = bag.split(" ")
        if count == "no":
            continue

        name = " ".join(name[:-1])
        count = 0 if count == "no" else int(count)
        bags.append((name, count))

    name = left.rsplit(" ", 1)[0]
    input[name] = bags

util.run(part1, part2, input)
