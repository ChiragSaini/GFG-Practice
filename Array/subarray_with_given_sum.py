t = int(input())
for _ in range(t):
    n, s = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    pivot = 0
    result = 0
    flag = False
    for i in range(n):
        result += arr[i]
        while(result > s):
            result -= arr[pivot]
            pivot += 1
        if result == s:
            print(pivot+1, i+1)
            flag = True
            break
    if flag == False:
        print(-1)
