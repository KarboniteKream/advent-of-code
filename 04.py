import re
import util


def part1(passports):
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valid = 0

    for passport in passports:
        ok = True

        for field in fields:
            if field not in passport:
                ok = False
                break

        if not ok:
            continue

        valid += 1

    return valid


def part2(passports):
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    ecls = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    valid = 0

    for passport in passports:
        ok = True

        for field in fields:
            if field not in passport:
                ok = False
                break

        if not ok:
            continue

        byr = passport["byr"]
        match = re.match(r"^\d{4}$", byr)
        if not (match and (1920 <= int(byr) <= 2002)):
            continue

        iyr = passport["iyr"]
        match = re.match(r"^\d{4}$", iyr)
        if not (match and (2010 <= int(iyr) <= 2020)):
            continue

        eyr = passport["eyr"]
        match = re.match(r"^\d{4}$", eyr)
        if not (match and (2020 <= int(eyr) <= 2030)):
            continue

        hgt = passport["hgt"]
        match_cm = re.match(r"^\d{3}cm$", hgt)
        match_in = re.match(r"^\d{2}in$", hgt)
        if not (match_cm and (150 <= int(hgt[:-2]) <= 193) or
                match_in and (59 <= int(hgt[:-2]) <= 76)):
            continue

        if not re.match(r"^#[a-f0-9]{6}$", passport["hcl"]):
            continue

        if passport["ecl"] not in ecls:
            continue

        if not re.match(r"^\d{9}$", passport["pid"]):
            continue

        valid += 1

    return valid


lines = util.read_lines("input/04.txt")
items = " ".join(line if line else "|" for line in lines).split("|")

passports = []
for item in items:
    passport = {}

    for field in item.split():
        key, value = field.split(":")
        passport[key] = value

    passports.append(passport)

util.run(part1, part2, passports)