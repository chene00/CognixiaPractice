"""
Task description
You are given two non-empty arrays A and B consisting of N integers. Arrays A and B represent N voracious fish in a river, ordered downstream along the flow of the river.

The fish are numbered from 0 to N − 1. If P and Q are two fish and P < Q, then fish P is initially upstream of fish Q. Initially, each fish has a unique position.

Fish number P is represented by A[P] and B[P]. Array A contains the sizes of the fish. All its elements are unique. Array B contains the directions of the fish. It contains only 0s and/or 1s, where:

0 represents a fish flowing upstream,
1 represents a fish flowing downstream.
If two fish move in opposite directions and there are no other (living) fish between them, they will eventually meet each other. Then only one fish can stay alive − the larger fish eats the smaller one. More precisely, we say that two fish P and Q meet each other when P < Q, B[P] = 1 and B[Q] = 0, and there are no living fish between them. After they meet:

If A[P] > A[Q] then P eats Q, and P will still be flowing downstream,
If A[Q] > A[P] then Q eats P, and Q will still be flowing upstream.
We assume that all the fish are flowing at the same speed. That is, fish moving in the same direction never meet. The goal is to calculate the number of fish that will stay alive.

For example, consider arrays A and B such that:

  A[0] = 4    B[0] = 0
  A[1] = 3    B[1] = 1
  A[2] = 2    B[2] = 0
  A[3] = 1    B[3] = 0
  A[4] = 5    B[4] = 0
Initially all the fish are alive and all except fish number 1 are moving upstream. Fish number 1 meets fish number 2 and eats it, then it meets fish number 3 and eats it too. Finally, it meets fish number 4 and is eaten by it. The remaining two fish, number 0 and 4, never meet and therefore stay alive.

Write a function:

def solution(A, B)

that, given two non-empty arrays A and B consisting of N integers, returns the number of fish that will stay alive.

For example, given the arrays shown above, the function should return 2, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [0..1,000,000,000];
each element of array B is an integer that can have one of the following values: 0, 1;
the elements of A are all distinct.
"""

# My Solution (BROKEN)

def solution(A, B):
    slow = 0
    count = 0
    # print(A)
    # print(B)
    # print("\n")
    for fast in range(1, len(A)):
        # print(f"{B[slow]} vs {B[fast]}")
        if B[slow] > B[fast]:
            # print("True")
            if A[slow] > A[fast]:
                # print("Slow is bigger")
                A[fast] = 'na'
                B[fast] = 'na'
            else:
                # print("Fast is bigger")
                A[slow] = 'na'
                B[slow] = 'na'
        if slow != 1:
            slow += 1
    for fish in B:
        if fish != 'na':
            count += 1
    return count
    pass

# Optimal Solution

def solution(A, B):
    survivors = 0
    downstream_fish = [] # This will act as our stack
    
    for i in range(len(A)):
        if B[i] == 1:
            # Fish is moving downstream. 
            # We don't know its fate yet, so we push its size onto the stack.
            downstream_fish.append(A[i])
        else:
            # Fish is moving upstream. It will fight any downstream fish in the stack.
            while len(downstream_fish) > 0:
                if downstream_fish[-1] < A[i]:
                    # The downstream fish is smaller, so it gets eaten.
                    # We pop it from the stack and continue the while loop 
                    # to fight the next downstream fish.
                    downstream_fish.pop()
                else:
                    # The downstream fish is bigger. 
                    # The upstream fish gets eaten, so we stop fighting.
                    break
            else:
                # The 'else' block of a 'while' loop in Python triggers ONLY 
                # if the loop didn't hit a 'break'.
                # This means the upstream fish ate ALL downstream fish (or the stack was empty).
                # Therefore, this upstream fish survives permanently.
                survivors += 1
                
    # Total survivors = upstream fish that survived + downstream fish still in the stack
    return survivors + len(downstream_fish)