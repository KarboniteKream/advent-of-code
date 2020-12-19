import util


def get_id(boarding_pass):
    row = (0, 127)
    col = (0, 7)

    for c in boarding_pass[:7]:
        mid = (row[0] + row[1]) // 2

        if c == "F":
            row = (row[0], mid)
        else: # B
            row = (mid + 1, row[1])

    for c in boarding_pass[7:]:
        mid = (col[0] + col[1]) // 2

        if c == "L":
            col = (col[0], mid)
        else: # R
            col = (mid + 1, col[1])

    return row[0] * 8 + col[0]


def part1(passes):
    max_id = 0

    for bp in passes:
        id = get_id(bp)
        max_id = max(id, max_id)

    return max_id


def part2(nums):
    ids = set()

    for bp in passes:
        id = get_id(bp)
        ids.add(id)

    for id in range(max(ids)):
        if id not in ids and (id - 1) in ids and (id + 1) in ids:
            return id


passes = util.read_lines("input/05.txt")
util.run(part1, part2, passes)
