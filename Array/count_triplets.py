# from collections import defaultdict
# * Accepted
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     s = set(arr)
#     res = 0
#     for i in range(n-1):
#         for j in range(i+1, n):
#             if arr[i] + arr[j] in s:
#                 res += 1
#     print(res if res > 0 else -1)

# TODO: Can I do better?
# ! Not Completed Now
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     arr.sort()
#     s = set(arr)
#     res = 0
#     i = 0
#     j = i+1
#     while i < n:
#         if arr[i] + arr[j] in s:
#             res += 1
#             i += 1
#             j = i+1
#         if j == n-1 and i < n-1:
#             i += 1
#             j = i+1
#         else:
#             break
#         j += 1
#     print(res if res > 0 else -1)
