arr = [10, 20, 5, 0, 40, 7, 2]
k = 3

def solution(arr, k):
    current_sum = sum(arr[:k])
    current_max = current_sum

    for i in range(len(arr) - k):
        current_sum -= arr[i]
        current_sum += arr[i+k]

        if current_sum > current_max:
            current_max = current_sum

    return current_max


print(solution(arr, k))