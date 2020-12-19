import util


def part1(orbits):
    result = 0

    for planet in orbits.keys():
        while planet != "COM":
            planet = orbits[planet]
            result += 1

    return result


def part2(orbits):
    def get_visits(name):
        visits = {}
        distance = 0

        while name != "COM":
            name = orbits[name]
            visits[name] = distance
            distance += 1

        return visits

    you = get_visits("YOU")
    santa = get_visits("SAN")

    intersection = set(you.keys()) & set(santa.keys())
    return min(map(lambda p: you[p] + santa[p], intersection))


data = util.read_lines("input/06.txt", lambda l: l.split(")"))
orbits = {right: left for left, right in data}
util.run(part1, part2, orbits)
