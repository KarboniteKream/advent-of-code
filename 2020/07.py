import util


def part1(input):
    data = {}

    for name, bags in input.items():
        for bag, _ in bags:
            data.setdefault(bag, []).append(name)

    def get_parent_bags(name):
        if name not in data:
            return {name}

        bags = set(data[name])
        for bag in data[name]:
            bags |= get_parent_bags(bag)
        return bags

    return len(get_parent_bags("shiny gold"))


def part2(input):
    def get_total_bags(name):
        total = 0
        for bag, count in input[name]:
            total += count + (count * get_total_bags(bag))
        return total

    return get_total_bags("shiny gold")


rules = util.read_lines("input/07.txt")
input = {}

for rule in rules:
    left, right = rule.split(" bags contain ")
    input[left] = []

    for bag in right.split(", "):
        count, *name = bag.split(" ")
        if count == "no":
            continue

        name = " ".join(name[:-1])
        count = 0 if count == "no" else int(count)
        input[left].append((name, count))

util.run(part1, part2, input)
