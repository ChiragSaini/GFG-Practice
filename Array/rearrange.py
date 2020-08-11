for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    max_idx = n-1
    min_idx = 0
    max_elem = arr[n-1] + 1
    for i in range(n):
        # print(f"Arr at begining of loop:{arr}")
        if i % 2 == 0:
            arr[i] += (arr[max_idx] % max_elem) * max_elem
            max_idx -= 1
        else:
            arr[i] += (arr[min_idx] % max_elem) * max_elem
            min_idx += 1
        # print(f"Arr at end of loop:{arr}")
        print("-"*50)
    for i in range(n):
        arr[i] = arr[i] // max_elem
    print(*arr)
