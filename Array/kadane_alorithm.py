for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    # Checking if all are negative
    all_are_negative = True
    for i in range(n):
        if arr[i] > 0:
            all_are_negative = False
    if all_are_negative:
        print(max(arr))
    else:
        max_ending_here = 0
        max_so_far = 0
        for i in range(n):
            max_ending_here += arr[i]
            if max_ending_here < 0:
                max_ending_here = 0
            max_so_far = max(max_so_far, max_ending_here)
        print(max_so_far)

# for _ in range(int(input())):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     max_ending_here = 0
#     max_so_far = 0
#     for i in range(n):
#         max_ending_here += + arr[i]
#         if max_ending_here < 0:
#             max_ending_here = 0
#         max_so_far = max(max_so_far, max_ending_here)
#     print(max_so_far)
