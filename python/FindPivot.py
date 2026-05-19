def solution(A):
    left_sum = 0
    right_sum = sum(A) - A[0]

    if len(A) == 1:
        return A

    for i in range(len(A)):
        if left_sum == right_sum:
            return i
        else:
            if i+1 >= len(A):
                break
            left_sum += A[i]
            right_sum -= A[i+1]

    return -1

def solution2(A):
    right_sum = sum(A)
    left_sum = 0

    for i in range(len(A) - 1):
        right_sum -= A[i]

        if (right_sum == left_sum):
            return i

        left_sum += A[i]

    return -1

A = [2, 1, -1]
print(solution(A))
print(solution2(A))
