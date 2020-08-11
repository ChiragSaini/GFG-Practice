t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    low, mid, high = 0, 0, n-1
    while mid <= high:
        if arr[mid] == 0:
            arr[mid], arr[low] = arr[low], arr[mid]
            low += 1
            mid += 1
        elif arr[mid] == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
        else:
            mid += 1
    print(*arr)
