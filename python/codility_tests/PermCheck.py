"""
Task description
A non-empty array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
is a permutation, but array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

Write a function:

def solution(A)

that, given an array A, returns 1 if array A is a permutation and 0 if it is not.

For example, given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
the function should return 1.

Given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
the function should return 0.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [1..1,000,000,000].
"""

# My Inital Solution

def solution(A):
    N = len(A)
    print(f"Length is : {length}")
    print(f"Max_Int is: {max_int}")

    total = sum(A)
    real_total = (N * (N + 1)) // 2
    diff = real_total - total
    print(N)
    print(diff)

    if diff == 0:
        return 1
    else:
        return 0
    pass

# My Improved Solution O(nlogn) python .sort() takes O(nlogn)

def solution(A):
    A.sort()
    # print(A)
    for i, v in enumerate(A):
        if (i + 1) != v:
            return 0
    
    return 1
    pass

# Optimal Solution

def solution(A):
    N = len(A)
    
    # Converting the array to a set removes all duplicates.
    unique_elements = set(A)
    
    # 1. Did we lose any elements to duplicates? (len(unique_elements) == N)
    # 2. Is the highest number exactly equal to the length? (max(unique_elements) == N)
    if len(unique_elements) == N and max(unique_elements) == N:
        return 1
        
    return 0