nums = [10, 20, 5, 40, 5, 20, 50]
nums_sorted = [10, 20, 5, 40, 5, 20, 50]
# [5, 5, 10, 20, 20, 40, 50]

from collections import Counter

def removeDupeHash(nums):

    freq = Counter(nums).items()
    output = []
    for key, value in freq:
        output.append(key)
    return output

print(f"Using Hash: {removeDupeHash(nums)}")

def fastSlow(nums):
    print(f"Sorted: {nums}")
    slow = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[slow]:
            slow += 1
            nums[slow] = nums[i]

    return slow + 1

nums_sorted.sort()
count = fastSlow(nums_sorted)

print(nums_sorted[:count])