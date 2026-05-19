"""
Task description
A non-empty array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.

Array A contains only 0s and/or 1s:

0 represents a car traveling east,
1 represents a car traveling west.
The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.

For example, consider array A such that:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the number of pairs of passing cars.

The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.

For example, given:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
"""

# My Solution

def solution(A):
    # Implement your solution here
    N = len(A)
    # [0, 1, 0, 1, 1]
    # [0, 1, 1, 2, 2, 2]
    count_zero_before = [0] * (N+1)
    for i in range(1, N + 1):
        if A[i-1] == 0:
            count_zero_before[i] = count_zero_before[i-1] + 1
        else:
            count_zero_before[i] = count_zero_before[i-1]

    total = 0
    for i, v in enumerate(A):
        if v == 1:
            total += count_zero_before[i]
        if total > 1000000000:
            return -1

    return total
    pass

# Optimal Solution

def solution(A):
    zeros_seen = 0
    total_passing = 0
    
    for car in A:
        if car == 0:
            # We see a car traveling East. We add to our tally.
            zeros_seen += 1
        elif car == 1:
            # We see a car traveling West. It passes ALL the East-bound 
            # cars we have seen up to this point.
            total_passing += zeros_seen
            
            # The required check for exceeding 1,000,000,000 pairs
            if total_passing > 1000000000:
                return -1
                
    return total_passing