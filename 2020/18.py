import operator
import util


def match_parenthesis(expr, idx):
    level = 0

    for offset, char in enumerate(expr[idx:]):
        level += (char == "(") - (char == ")")

        if char == ")" and level == 0:
            return idx + offset

    return None


def calculate(expr):
    acc = 0
    num, op = 0, operator.add
    idx = 0

    while idx < len(expr):
        char = expr[idx]

        if char.isdigit():
            num = (num * 10) + int(char)
        elif char == "+":
            acc = op(acc, num)
            num = 0
            op = operator.add
        elif char == "*":
            acc = op(acc, num)
            num = 0
            op = operator.mul
        elif char == "(":
            end = match_parenthesis(expr, idx)
            num = calculate(expr[idx + 1:end])
            idx = end

        idx += 1

    return op(acc, num)


def calculate_mul(expr):
    acc = 0
    idx = 0

    while idx < len(expr):
        char = expr[idx]

        if char.isdigit():
            num = expr[idx:].split(" ", 1)[0]
            acc += int(num)
            idx += len(num)
        elif char == "*":
            res = calculate_mul(expr[idx + 1:])
            acc = res if acc == 0 else acc * res
            break
        elif char == "(":
            end = match_parenthesis(expr, idx)
            acc += calculate_mul(expr[idx + 1:end])
            idx = end

        idx += 1

    return acc


def part1(exprs):
    return sum(calculate(expr) for expr in exprs)


def part2(exprs):
    return sum(calculate_mul(expr) for expr in exprs)


exprs = util.read_lines("input/18.txt")
util.run(part1, part2, exprs)
