"""
Task description
A small frog wants to get to the other side of a river. The frog is initially located on one bank of the river (position 0) and wants to get to the opposite bank (position X+1). Leaves fall from a tree onto the surface of the river.

You are given an array A consisting of N integers representing the falling leaves. A[K] represents the position where one leaf falls at time K, measured in seconds.

The goal is to find the earliest time when the frog can jump to the other side of the river. The frog can cross only when leaves appear at every position across the river from 1 to X (that is, we want to find the earliest moment when all the positions from 1 to X are covered by leaves). You may assume that the speed of the current in the river is negligibly small, i.e. the leaves do not change their positions once they fall in the river.

For example, you are given integer X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
In second 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river.

Write a function:

def solution(X, A)

that, given a non-empty array A consisting of N integers and integer X, returns the earliest time when the frog can jump to the other side of the river.

If the frog is never able to jump to the other side of the river, the function should return −1.

For example, given X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
the function should return 6, as explained above.

Write an efficient algorithm for the following assumptions:

N and X are integers within the range [1..100,000];
each element of array A is an integer within the range [1..X].
"""

# My Solution

def solution(X, A):
    N = len(A)
    if N < X:
        return -1

    leaves = {}

    for i, value in enumerate(A):
        # Instead of checking if its in the dict then skipping, just check if its not then append
        if value in leaves:
            continue
        else:
            leaves[value] = i
    
    # Remeber that range() in python is NOT INCLUSIVE need + 1 if we want to check up to N
    for i in range(1, X + 1):
        # Don't use .keys() because it actually creates a new dictionary. This is the same as just doing if i not in leaves
        if i not in leaves.keys():
            return -1

    return max(leaves.values())
    pass

# Optimal Solution

""" Need to remember if for some reason i need unique numbers. I can always try to use a set"""

def solution(X, A):
    # A set to keep track of the unique positions where leaves have fallen
    fallen_leaves = set()
    
    for time, position in enumerate(A):
        # We only care about leaves that fall between 1 and X
        if 1 <= position <= X:
            fallen_leaves.add(position)
        
        # As soon as our set has X unique leaves, the path is complete
        if len(fallen_leaves) == X:
            return time
            
    return -1