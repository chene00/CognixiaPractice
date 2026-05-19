"""
Task description
A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P - 1] and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P - 1]) - (A[P] + A[P + 1] + ... + A[N - 1])|

In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

For example, consider array A such that:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
We can split this tape in four places:

P = 1, difference = |3 - 10| = 7
P = 2, difference = |4 - 9| = 5
P = 3, difference = |6 - 7| = 1
P = 4, difference = |10 - 3| = 7
Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

For example, given:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [-1,000..1,000].
"""

# My Solution O(N*2) too long

import math
def solution(A):
  N = len(A)
  diff = []
  for p in range (1, N):
    # 
    diff.append(abs((sum(A[:p])) - sum(A[p:])))
  return min(diff)
  pass
  
# Optimized Solution

A = [2, 4, 5, 6]
def solution(A):
  right_sum = sum(A) # 17
  left_sum = 0 

  min_diff = float('inf')

  for p in range(len(A) - 1):
    left_sum += A[p] # 2 -> 6 -> 11
    right_sum -= A[p] # 15 -> 9 -> 4

    curr_diff = abs(right_sum - left_sum) # 15 - 2 = 13 -> 3 -> 4 - 11 = 7

    min_diff = min(curr_diff, min_diff) # 13 < inf -> 3 < 13 -> 7 not < 3

  return min_diff
