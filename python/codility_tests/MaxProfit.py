"""
An array A consisting of N integers is given. It contains daily prices of a stock share for a period of N consecutive days. If a single share was bought on day P and sold on day Q, where 0 ≤ P ≤ Q < N, then the profit of such transaction is equal to A[Q] − A[P], provided that A[Q] ≥ A[P]. Otherwise, the transaction brings loss of A[P] − A[Q].

For example, consider the following array A consisting of six elements such that:

  A[0] = 23171
  A[1] = 21011
  A[2] = 21123
  A[3] = 21366
  A[4] = 21013
  A[5] = 21367
If a share was bought on day 0 and sold on day 2, a loss of 2048 would occur because A[2] − A[0] = 21123 − 23171 = −2048. If a share was bought on day 4 and sold on day 5, a profit of 354 would occur because A[5] − A[4] = 21367 − 21013 = 354. Maximum possible profit was 356. It would occur if a share was bought on day 1 and sold on day 5.

Write a function,

def solution(A)

that, given an array A consisting of N integers containing daily prices of a stock share for a period of N consecutive days, returns the maximum possible profit from one transaction during this period. The function should return 0 if it was impossible to gain any profit.

For example, given array A consisting of six elements such that:

  A[0] = 23171
  A[1] = 21011
  A[2] = 21123
  A[3] = 21366
  A[4] = 21013
  A[5] = 21367
the function should return 356, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..400,000];
each element of array A is an integer within the range [0..200,000].
"""

# Optimal Solution

def solution(A):
    # If the array is empty or has only 1 day, no profit can be made
    if len(A) < 2:
        return 0

    # Start by assuming the first day is the cheapest price
    min_price = A[0]
    max_profit = 0

    for price in A:
        # 1. Is today's price cheaper than our lowest recorded price?
        if price < min_price:
            min_price = price
            
        # 2. If we sold today, is the profit better than our best recorded profit?
        else:
            current_profit = price - min_price
            if current_profit > max_profit:
                max_profit = current_profit

    return max_profit