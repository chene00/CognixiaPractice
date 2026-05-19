"""
Task Description

A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

Write a function:

class Solution { public int solution(int N); }

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].
"""

# My Solution

def solution(N):
    binary = []
    start = 'none'
    current_zero = 0
    current_max = 0

    # Build the binary representation of the number
    while N > 0:
        bit = N % 2
        binary.append(bit)
        N = N // 2

    binary.reverse()

    for bit in binary:
        # If its the first 1 we see, start the counting
        if bit == 1 and start == 'none':
            start = 'saw 1'
        elif bit == 0 and start == 'saw 1':
            current_zero += 1
        elif bit == 1 and start == 'saw 1':
            if current_zero > current_max:
                current_max = current_zero
            current_zero = 0
    return current_max
    pass

# Optimal Solution

def solution2(N):
    longest_gap = 0
    current_gap = 0
    # Start at zero to disregard the intial zeros that aren't surrounded by 1s
    counting_gap = False
    
    while N > 0:
        if N & 1 == 1:
            # If we saw a 1 earlier then that means we just finished a gap
            if counting_gap:
              
                longest_gap = max(longest_gap, current_gap)

            # Reset the gap
            counting_gap = True
            current_gap = 0
        else:
            
            # If we saw a 1 then we can start counting, removes the trailing zeros
            if counting_gap:
                current_gap += 1

        # Bit shift 1 to the right same as N //= 2
        N >>= 1
    
    return longest_gap