import collections
import util


def part1(groups):
    result = 0

    for group in groups:
        answers = set(group.replace("\n", ""))
        result += len(answers)

    return result


def part2(groups):
    result = 0

    for group in groups:
        people = group.split()
        answers = collections.defaultdict(int)

        for person in people:
            for answer in person:
                answers[answer] += 1

        for answer in answers.values():
            if answer == len(people):
                result += 1

    return result


groups = util.read("input/06.txt").split("\n\n")
util.run(part1, part2, groups)
