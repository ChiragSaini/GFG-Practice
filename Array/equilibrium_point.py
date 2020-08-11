t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if n == 1:
        print(1)
    else:
        back = sum(arr) - arr[0] - arr[1]
        front = arr[0]
        res = -1
        for i in range(1, n-1):
            # print(f"Front:{front}, Back:{back}")
            if front == back:
                res = i+1
                break
            front += arr[i]
            back -= arr[i+1]
        # for i in range(n-1):
        #     front = sum(arr[:i])
        #     back = sum(arr[i+1:])
        #     if front == back:
        #         res = i+1
        print(res)
