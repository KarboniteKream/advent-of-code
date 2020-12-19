import util


def get_visits(name):
    visits = {}
    distance = 0

    while name != "COM":
        name = orbits[name]
        visits[name] = distance
        distance += 1

    return visits


data = util.read_lines("input/06.txt", lambda l: l.split(")"))
orbits = {right: left for [left, right] in data}

you = get_visits("YOU")
santa = get_visits("SAN")

intersection = set(you.keys()) & set(santa.keys())
result = min(map(lambda p: you[p] + santa[p], intersection))

print(result)
