"""
Task Description

An array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index, and the last element of the array is moved to the first place. For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the first place).

The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.

Write a function:

class Solution { public int[] solution(int[] A, int K); }

that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.

For example, given

    A = [3, 8, 9, 7, 6]
    K = 3
the function should return [9, 7, 6, 3, 8]. Three rotations were made:

    [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
    [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
    [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
For another example, given

    A = [0, 0, 0]
    K = 1
the function should return [0, 0, 0]

Given

    A = [1, 2, 3, 4]
    K = 4
the function should return [1, 2, 3, 4]

Assume that:

N and K are integers within the range [0..100];
each element of array A is an integer within the range [-1,000..1,000].
In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
"""

# My Solution

def solution(A, K):
    N = len(A)
    new_arr = [0] * N
    for i, value in enumerate(A):
        new_index = (i + K) % N
        new_arr[new_index] = value

    return new_arr
    pass

# Optimized Solution

def solution(A, K):
    if not A: # Quick check for empty array
        return A
        
    # Simplify K in case K is larger than the array length
    K = K % len(A)
    
    if K == 0:
        return A
        
    # A[-K:] gets the last K elements
    # A[:-K] gets everything else
    return A[-K:] + A[:-K]

# Space Complexity Optimized 

def reverse_portion(arr, start, end):
    # This loop swaps the outer elements, moving inward until they meet
    while start < end:
        arr[start], arr[end] = arr[end], arr[start] # Python's quick swap trick
        start += 1
        end -= 1

def solution(A, K):
    N = len(A)
    # Gu    ard clauses
    if N == 0: 
        return A
        
    K = K % N # Simplify K
    if K == 0: 
        return A

    # Step 1: Reverse the whole array
    reverse_portion(A, 0, N - 1)
    
    # Step 2: Reverse the first K elements
    reverse_portion(A, 0, K - 1)
    
    # Step 3: Reverse the remaining elements
    reverse_portion(A, K, N - 1)

    return A