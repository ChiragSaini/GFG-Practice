for _ in range(int(input())):
    x, y = map(int, input().split())
    arr_x = list(map(int, input().split()))
    arr_y = list(map(int, input().split()))
    i = 0
    j = 0
    while i < x and j < y:
        if arr_x[i] > arr_y[j]:
            arr_x[i], arr_y[j] = arr_y[j], arr_x[i]
            i += 1
        else:
            j += 1
    print(f"arr_x:{arr_x}")
    print(f"arr_y:{arr_y}")
# ! Incomplete and Shitty Soln. Just Like Me.
