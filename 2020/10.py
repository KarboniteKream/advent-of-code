import collections
import util


def part1(nums):
    nums = sorted(nums)
    nums = [0, *nums, nums[-1] + 3]

    diffs = collections.defaultdict(int)
    for i in range(1, len(nums)):
        diffs[nums[i] - nums[i - 1]] += 1

    return diffs[1] * diffs[3]


def part2(nums):
    nums = sorted(nums)
    nums = [0, *nums, nums[-1] + 3]

    target = nums[-1]
    nums = set(nums)

    counts = collections.defaultdict(int)

    def get_count(num):
        if num in counts:
            return counts[num]

        if num not in nums:
            counts[num] = 0
            return 0

        if num == target:
            counts[num] = 1
            return 1

        for i in range(1, 4):
            counts[num] += get_count(num + i)

        return counts[num]

    return get_count(0)


nums = util.read_lines("input/10.txt", int)
util.run(part1, part2, nums)
