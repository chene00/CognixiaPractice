# O(n) implementation

def twoSum(nums, targetSum : int):
    # Intialize a dictioanry
    seenNums = {}

    # Iterate through the list O(n)
    for i, num in enumerate(nums):
        compliment = targetSum - num
        # O(1) because we are comparing against a Dictionary so Python can calcualte without having to loop through
        if compliment in seenNums.keys():
            return [i, seenNums[compliment]]
        else:
            # Add number to dictionary starting at 1
            seenNums[num] = i
    return [-1, -1]

def twoSumSorted(nums, targetSum: int):
    left = 0
    right = len(nums) - 1

    while left < right:

        currentSum = nums[left] + nums[right]

        if currentSum > targetSum:
            right -= 1
        elif currentSum < targetSum:
            left += 1
        else:
            return [left, right]

    return [-1, -1]

if __name__ == "__main__":
    numbers = [10, 20, 0, 30, 50, 5, 7]
    sortedNumbers = sorted(numbers)
    print(sortedNumbers)
    targetSum = 27;

    print(twoSum(numbers, targetSum))
    print(twoSumSorted(sortedNumbers, targetSum))