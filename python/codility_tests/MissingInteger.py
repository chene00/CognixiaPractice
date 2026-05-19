"""
Task description
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""

# My Solution

from collections import Counter
def solution(A):
    length = len(A)
    freq = Counter(A)
    ans = 1
    for i in range(length+1):
        # print(f"Checking if {ans} in freq")
        if ans in freq:
            ans += 1
        else:
            return ans
    pass

# Optimized Solution
""" 
I need to remember if just want to check someone against a list to make sure it exist or doesnt exist i can just use a 
set instead of a dict
"""
def solution(A):
    # Convert to a set to remove duplicates and enable O(1) lookups
    seen = set(A)
    
    ans = 1
    # Keep incrementing 'ans' until we find a number that isn't in the set
    while ans in seen:
        ans += 1
        
    return ans