from typing import List


def findNumbers(nums: List[int]) -> int:
    even = 0
    for i in nums:
        count = 0
        while i > 0:
            i = i // 10
            count += 1

        if count % 2 == 0:
            even += 1
    print(even)


# findNumbers([123, 12])


def findNumbers2(nums: List[int]) -> int:
    nums = map(str, nums)
    print(nums)
    count = 0
    for i in nums:
        if len(i) % 2 == 0:
            count += 1
    return count


print(findNumbers2([123, 34]))
