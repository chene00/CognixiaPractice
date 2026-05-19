"""
Task description
Write a function:

def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.
"""

# My Solution

def solution(A, B, K):
    divisible = 0
    for i in range(A, B+1):
        if i % K == 0:
            divisible += 1

    return divisible
    pass

# Optimal Solution

def solution(A, B, K):
    # Calculate multiples up to B, minus multiples up to A
    divisible = (B // K) - (A // K)
    
    # If A itself is divisible by K, we need to count it too
    if A % K == 0:
        divisible += 1
        
    return divisible