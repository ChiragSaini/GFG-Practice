t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print((n*(n+1)) // 2 - sum(arr))
