import collections
import re
import util


def in_range(field, ranges):
    return any(r[0] <= field <= r[1] for r in ranges)


def is_valid(ticket, ranges):
    for field in ticket:
        if not in_range(field, ranges):
            return False, field

    return True, None


def part1(rules, tickets):
    ranges = [r for rule in rules.values() for r in rule]

    errors = 0
    for ticket in tickets[1:]:
        ok, field = is_valid(ticket, ranges)
        if not ok:
            errors += field

    return errors


def part2(rules, tickets):
    ranges = [r for rule in rules.values() for r in rule]
    tickets = [ticket for ticket in tickets if is_valid(ticket, ranges)[0]]

    candidates = collections.defaultdict(set)
    for idx in range(len(tickets[0])):
        for name, ranges in rules.items():
            if all(in_range(ticket[idx], ranges) for ticket in tickets):
                candidates[name].add(idx)

    names = {}
    while candidates:
        for name, idx in candidates.items():
            if len(idx) == 1:
                break

        idx = idx.pop()
        names[name] = idx
        del candidates[name]

        for name in candidates:
            candidates[name].remove(idx)

    result = 1
    for name, idx in names.items():
        if name.startswith("departure"):
            result *= tickets[0][idx]

    return result


sections = util.read("input/16.txt").split("\n\n")
fields, my, nearby = map(lambda s: s.split("\n"), sections)

rules = {}
for field in fields:
    name, *ranges = re.match(r"(.*): (\d+-\d+) or (\d+-\d+)", field).groups()
    rules[name] = [tuple(map(int, r.split("-"))) for r in ranges]

tickets = [list(map(int, t.split(","))) for t in my[1:] + nearby[1:-1]]
util.run(part1, part2, rules, tickets)
