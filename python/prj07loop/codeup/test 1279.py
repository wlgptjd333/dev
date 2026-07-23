#1279
# a, b = map(int, input().split())
# num = 0
# for i in range(a, b + 1):
#     if i % 2 == 0:
#         num -= i
#     else:
#         num += i
# print(num)
from calendar import firstweekday

#1280
# a, b = map(int, input().split())
# num = 0
# for i in range(a, b + 1):
#     if i % 2 == 0:
#         print(f"-{i}", end="")
#         num -= i
#     else:
#         print(f"+{i}", end="")
#         num += i
# print(f"={num}")
#
# 1281
# a, b = map(int, input().split())
# num = 0
# for i in range(a, b + 1):
#     if i % 2 == 0:
#         print(f"-{i}", end="")
#         num -= i
#     else:
#         if i == a:
#             print(i, end="")
#             num += i
#         else:
#             print(f"+{i}", end="")
#             num += i
# print(f"={num}")

# 1274
# n = int(input())
#
# for i in range(2, n + 1):
#     if n % i == 0:
#         print("not prime")
#         break
# else:
#     print("prime")

# 1276
# n = int(input())
# num = 1
# for i in range(1, n+1):
#     num = num*i
# print(num)

# 1256
# n = int(input())
# for i in range(n):
#     print("*", end="")

# 1277
# N = int(input())
# num_list = list(map(int, input().split()))
# print(num_list[0],num_list[N//2], num_list[-1])