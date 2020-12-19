import util

def is_valid(number):
    digits = str(number)
    count = [0] * 10
    count[int(digits[5])] = 1

    for i in range(5):
        if digits[i] > digits[i + 1]:
            return False

        count[int(digits[i])] += 1

    return 2 in count


[low, high] = list(map(int, util.read_line("input/04.txt").split("-")))

result = sum(1 for num in range(low, high + 1) if is_valid(num))
print(result)
