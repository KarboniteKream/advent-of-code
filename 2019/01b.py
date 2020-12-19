import util

modules = util.read_lines("input/01.txt", int)
fuel = 0

for mass in modules:
    while mass > 0:
        mass = max(mass // 3 - 2, 0)
        fuel += mass

print(fuel)
