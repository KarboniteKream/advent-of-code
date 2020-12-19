import util


def find_sum(nums, target):
    seen = set()

    for num in nums:
        if (target - num) in seen:
            return True

        seen.add(num)

    return False


def part1(nums):
    for i in range(25, len(nums)):
        if not find_sum(nums[i - 25:i], nums[i]):
            return nums[i]


def part2(nums):
    target = part1(nums)

    for i in range(0, len(nums)):
        sum = 0

        for j in range(i, len(nums)):
            sum += nums[j]

            if sum == target and abs(i - j) > 1:
                arr = sorted(nums[i:j + 1])
                return arr[0] + arr[-1]


nums = util.read_lines("input/09.txt", int)
util.run(part1, part2, nums)
