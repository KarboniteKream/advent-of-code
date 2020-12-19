import util


def part1(nums):
    seen = set()

    for num in nums:
        other = 2020 - num
        if other in seen:
            return num * other

        seen.add(num)


def part2(nums):
    seen = set(nums)

    for i, num1 in enumerate(nums):
        for num2 in nums[i + 1:]:
            other = 2020 - num1 - num2
            if other in seen:
                return num1 * num2 * other


nums = util.read_lines("input/01.txt", int)
util.run(part1, part2, nums)
