import util

data = list(map(int, list(util.read_line("input/08.txt"))))

width, height = 25, 6
layers = len(data) // (width * height)

image = [[2 for x in range(width)] for y in range(height)]

for layer in range(layers):
    z = layer * width * height

    for y in range(height):
        for x in range(width):
            if image[y][x] == 2:
                image[y][x] = data[z + (y * width) + x]

for y in range(height):
    for x in range(width):
        print("O" if image[y][x] == 1 else ".", end="")

    print()
