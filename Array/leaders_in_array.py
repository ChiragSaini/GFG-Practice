t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if n == 1:
        print(arr[0])
    else:
        leaders = [arr[-1], ]
        bigger = arr[-1]
        for i in range(n-2, -1, -1):
            if arr[i] >= bigger:
                leaders.append(arr[i])
                bigger = arr[i]
        print(*list(reversed(leaders)))
