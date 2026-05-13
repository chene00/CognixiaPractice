"""
Divide the input array into single element arrays. Then call the merge function to compare
all the elements in the left and right arrays and then merge them.
"""

def mergeSort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    # Recursively break down the left and right half until there are only 1 element in the array.
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    # The mergeSort call will return and start calling merge on the halfs.

    return merge(left, right)

"""
Instead of using recursion to divide the input array into single element arrays. 
For Iterative sort we just split the array in a certain way where we only compare single
element "arrays" with each other and merge them. So instead of actually dividing the arrays
we just use the input one and slice it in certain ways to get single element arrays. 
"""
def iterativeSort(arr):
    if len(arr) <= 1:
        return arr
    
    n = len(arr)
    width = 1

    while width < n:
        for i in range(0, n, 2*width):
            left = arr[i: i + width]
            right = arr[i+width : i + 2* width]

            arr[i:i+2*width] = merge(left, right)

        width *= 2

    return arr

"""
The merge function that is used to compare two arrays and then return a sorted array.
"""
def merge(left, right):
    sorted_array = []
    i = 0
    j = 0

    # Compare the already sorted arrays. Adding all items in correct order.
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        elif right[j] < left[i]:
            sorted_array.append(right[j])
            j += 1

    # Add any left overs since its already sorted
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array

if __name__ == "__main__":

    list = [70, 30, 50, 10]

    print(mergeSort(list))
    print(iterativeSort(list))

