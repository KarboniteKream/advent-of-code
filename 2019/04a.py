import util

def is_valid(number):
    digits = str(number)
    valid = False

    for i in range(5):
        if digits[i] > digits[i + 1]:
            return False

        if digits[i] == digits[i + 1]:
            valid = True

    return valid


[low, high] = list(map(int, util.read_line("input/04.txt").split("-")))

result = sum(1 for num in range(low, high + 1) if is_valid(num))
print(result)
