"""
Task description
You are given N counters, initially set to 0, and you have two possible operations on them:

increase(X) − counter X is increased by 1,
max counter − all counters are set to the maximum value of any counter.
A non-empty array A of M integers is given. This array represents consecutive operations:

if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
if A[K] = N + 1 then operation K is max counter.
For example, given integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the values of the counters after each consecutive operation will be:

    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)
The goal is to calculate the value of every counter after all operations.

Write a function:

def solution(N, A)

that, given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers representing the values of the counters.

Result array should be returned as an array of integers.

For example, given:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the function should return [3, 2, 2, 4, 2], as explained above.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..100,000];
each element of array A is an integer within the range [1..N + 1].
"""

# My Solution O(N * M) (M is size of A)

def solution(N, A):
    counters = [0] * N

    for k in A:
        if k == N + 1:
            ounters = [max(counters)] * N

        else:
            counters[k - 1] += 1
    return counters
pass

# Optimized Solution O(N + M)

def solution(N, A):
    counters = [0] * N

    # Use counters to track the current max and if set all max has been called
    base_max = 0
    current_max = 0

    for k in A:
        if k == N + 1:

            # Instead of actually updating the max, keep the number and then update the end
            base_max = current_max
        else:
            idx = k - 1

            # Since we aren't actually updating it. If a counter is being incremented but hasn't been updated to base_max
            # update first before incrementing

            if counters[idx] < base_max:
                counters[idx] = base_max

            counters[idx] += 1

            if counters[idx] > current_max:
                current_max = counters[idx]
            
        
    # Update rest of counters to max
    for i in range(N):
        if counters[i] < base_max:
            counters[i] = base_max

    return counters