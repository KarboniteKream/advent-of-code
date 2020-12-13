import util


def part1(timestamp, buses):
    buses = list(filter(lambda bus: bus != "x", buses))
    deltas = {}

    for bus in buses:
        time = 0
        while time < timestamp:
            time += bus
        deltas[bus] = time - timestamp

    bus = min(deltas, key=deltas.get)
    return bus * deltas[bus]


def part2(_, buses):
    timestamp = 0
    delta = 1
    idx = 0

    while idx < len(buses):
        bus = buses[idx]

        if bus == "x":
            idx += 1
            continue

        if (timestamp + idx) % bus == 0:
            delta *= bus
            idx += 1
            continue

        timestamp += delta

    return timestamp


notes = util.read_lines("input/13.txt")
timestamp = int(notes[0])
buses = [int(bus) if bus != "x" else bus for bus in notes[1].split(",")]
util.run(part1, part2, timestamp, buses)
