"""
Task description
A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a slice of array A (notice that the slice contains at least two elements). The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

For example, array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
contains the following example slices:

slice (1, 2), whose average is (2 + 2) / 2 = 2;
slice (3, 4), whose average is (5 + 1) / 2 = 3;
slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
The goal is to find the starting position of a slice whose average is minimal.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the starting position of the slice with the minimal average. If there is more than one slice with a minimal average, you should return the smallest starting position of such a slice.

For example, given array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−10,000..10,000].
"""

# My Solution - Only checking slice of size 2 because i thought slice of size 2 is the smallest. However, slices of size 3 
# could also be a possbility. should've added that check. Also instead of using a precomputed pre-fix some. We can just 
# check the element + next and the element + next + next avg.

def solution(A):
    N = len(A)
    prefix = [0] * (N+1)
    for i in range (1, N+1):
        prefix[i] = prefix[i-1] + A[i-1]

    # print(prefix)

    slow = 0
    small_value = float('inf')
    small_index = -1
    average = []
    for fast in range(2, N + 1):
        avg = (prefix[fast] - prefix[slow]) / 2
        average.append(avg)
        if avg < small_value:
            small_index = slow
            small_value = avg
        slow += 1
    return small_index
    pass

# [4, 2, 2, 5, 1, 5, 8]
# [0, 4, 6, 8, 13, 14, 19, 27]

# Optimal Solution

def solution(A):
    N = len(A)
    
    # We use infinity as our starting "minimum" so the first real average overwrites it
    min_avg = float('inf')
    min_index = -1
    
    for i in range(N - 1):
        # 1. Check the slice of length 2
        avg_2 = (A[i] + A[i+1]) / 2.0
        if avg_2 < min_avg:
            min_avg = avg_2
            min_index = i
            
        # 2. Check the slice of length 3 (We must ensure i+2 doesn't go out of bounds!)
        if i < N - 2:
            avg_3 = (A[i] + A[i+1] + A[i+2]) / 3.0
            if avg_3 < min_avg:
                min_avg = avg_3
                min_index = i
                
    return min_index