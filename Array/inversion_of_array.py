def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    half = len(arr) // 2
    left = arr[:half]
    right = arr[half:]
    return merge(left, right)


def merge(left, right):
    i = 0
    j = 0
    result = []
    size_left = len(left)
    size_right = len(right)
    inversions = 0
    while i < size_left and j < size_right:
        if left[i] > right[j] and i < j:
            inversions += 1
            j += 1
        else:
            i += 1
    return inversions


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(mergeSort(arr))
