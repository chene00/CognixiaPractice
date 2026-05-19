
"""
Task description

An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

def solution(A)

that, given an array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].
"""

# My solution. Didn't work.

def solution(A):
    A_sorted = sorted(A)
    prev = 0    
    # enumerate() starting at 1 just moves the index value to 1. the actual value is still at the first element
    for i, value in enumerate(A_sorted, start=1):
        diff = value - A_sorted[0]
        if diff > 1:
            return i + 1
        prev = i
    pass

# Optimized Solution 1

def solution(A):
    # N is the length of the array
    N = len(A)
    
    # The array SHOULD contain numbers up to N + 1
    max_num = N + 1
    
    # Mathematical formula for the sum of numbers from 1 to max_num
    # Formula: (n * (n + 1)) // 2
    expected_sum = (max_num * (max_num + 1)) // 2
    
    # The actual sum of the array we were given
    actual_sum = sum(A)
    
    # The missing number is simply the difference
    return expected_sum - actual_sum

# Optimized Solution 2

def solution(A):
    missing_number = 0
    
    # XOR all the numbers that SHOULD be in the array (1 to N+1)
    for i in range(1, len(A) + 2):
        missing_number ^= i
        
    # XOR all the numbers that are ACTUALLY in the array
    for value in A:
        missing_number ^= value
        
    return missing_number