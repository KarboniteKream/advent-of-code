import util

data = list(map(int, list(util.read_line("input/08.txt"))))

width, height = 25, 6
layers = len(data) // (width * height)

result = (None, 0)

for layer in range(layers):
    z = layer * width * height
    count = [0, 0, 0]

    for y in range(height):
        for x in range(width):
            count[data[z + (y * width) + x]] += 1

    if result[0] is None or count[0] < result[0]:
        result = (count[0], count[1] * count[2])

print(result[1])
