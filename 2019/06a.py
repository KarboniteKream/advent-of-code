import util

data = util.read_lines("input/06.txt", lambda l: l.split(")"))
orbits = {right: left for [left, right] in data}

result = 0

for planet in orbits.keys():
    while planet != "COM":
        planet = orbits[planet]
        result += 1

print(result)
