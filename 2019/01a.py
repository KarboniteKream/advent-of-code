import util

modules = util.read_lines("input/01.txt", int)
fuel = 0

for mass in modules:
    fuel += mass // 3 - 2

print(fuel)
