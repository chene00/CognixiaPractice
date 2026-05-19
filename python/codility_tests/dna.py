"""
Task description
A DNA sequence can be represented as a string consisting of the letters A, C, G and T, which correspond to the types of successive nucleotides in the sequence. Each nucleotide has an impact factor, which is an integer. Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4, respectively. You are going to answer several queries of the form: What is the minimal impact factor of nucleotides contained in a particular part of the given DNA sequence?

The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters. There are M queries, which are given in non-empty arrays P and Q, each consisting of M integers. The K-th query (0 ≤ K < M) requires you to find the minimal impact factor of nucleotides contained in the DNA sequence between positions P[K] and Q[K] (inclusive).

For example, consider string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
The answers to these M = 3 queries are as follows:

The part of the DNA between positions 2 and 4 contains nucleotides G and C (twice), whose impact factors are 3 and 2 respectively, so the answer is 2.
The part between positions 5 and 5 contains a single nucleotide T, whose impact factor is 4, so the answer is 4.
The part between positions 0 and 6 (the whole string) contains all nucleotides, in particular nucleotide A whose impact factor is 1, so the answer is 1.
Write a function:

def solution(S, P, Q)

that, given a non-empty string S consisting of N characters and two non-empty arrays P and Q consisting of M integers, returns an array consisting of M integers specifying the consecutive answers to all queries.

Result array should be returned as an array of integers.

For example, given the string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
the function should return the values [2, 4, 1], as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
M is an integer within the range [1..50,000];
each element of arrays P and Q is an integer within the range [0..N - 1];
P[K] ≤ Q[K], where 0 ≤ K < M;
string S consists only of upper-case English letters A, C, G, T.
"""


# My Solution

def solution(S, P, Q):
    N = len(S)
    impact = [0] * N
    for i in range(N):
        if S[i] == 'A':
            impact[i] = 1
        elif S[i] == 'C':
            impact[i] = 2
        elif S[i] == 'G':
            impact[i] = 3
        else:
            impact[i] = 4

    answer = []
    for i in zip(P, Q):
        left = i[0]
        right = i[1]
        curr_min = float('inf')
        for j in range(left, right+1):
            if impact[j] < curr_min:
                curr_min = impact[j]

        answer.append(curr_min)

    return answer

    
    # [C, A, G, C, C, T, A]
    # [2, 1, 3, 2, 2, 4, 1]
    # [0, 2, 3, 6, 8, 10, 14, 15]
    # [0, 2, 1, 1, 1, 1, 1, 1]
    #        ^     ^
    pass

# Optimal Solution
"""
Use 3 prefix sum arrays to track A, C, and G.
Logic behind this solution is to keep track of how manys A, C, and G we saw at a certain point in the DNA sequence.
At the end when we need the answer, check if there were any A's between the two indexes, if so then return 1 because A is smallest. Continue
from smallest to largest.
"""

def solution(S, P, Q):
    N = len(S)
    a = [0] * (N+1)
    c = [0] * (N+1)
    g = [0] * (N+1)
    for i in range(1, N+1):
        a[i] = a[i-1]
        c[i] = c[i-1]
        g[i] = g[i-1]

        if S[i-1] == 'A':
            a[i] += 1
        elif S[i-1] == 'C':
            c[i] += 1
        elif S[i-1] == 'G':
            g[i] += 1

    ans = []
    for i in zip(P, Q):
        left = i[0]
        right = i[1] + 1

        if a[right] - a[left] > 0:
            ans.append(1)
        elif c[right] - c[left] > 0:
            ans.append(2)
        elif g[right] - g[left] > 0:
            ans.append(3)
        else:
            ans.append(4)
    
    return ans
    pass