from collections import Counter
t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    arr_x = list(map(int, input().split()))
    arr_y = list(map(int, input().split()))
    res = 0
    # * Naive Solution ==> Obviously Dosen't work
    # for i in range(x):
    #     for j in range(y):
    #         if arr_x[i]**arr_y[j] > arr_y[j]**arr_x[i]:
    #             res += 1
    # print(res)
    # * Effective Aproach
    arr_y.sort()
    if x == 0:
        print(0)
    elif x == 1:
        c = Counter(y)
        print(c[0])
    else:
        for i in range(x):
            for j in range(y):
                if arr_y[j] > arr_x[i]:
                    if arr_y[j] == 4 or arr_y[j] == 3:
                        res -= 1
                    else:
                        res += 1
                    break
        print(res)
