# a = int(input())
# if a == 1 or a == 3 or a == 5 or a == 7:
#     print("oh my god")
# else:
#     print("enjoy")
#
# a, b = map(int, input().split())
#
# if a%2 == 0:
#     if b%2 == 0:
#         print("짝수+짝수=짝수")
#     else:
#         print("짝수+홀수=홀수")
# else:
#     if b%2 == 0:
#         print("홀수+짝수=홀수")
#     else:
#         print("홀수+홀수=짝수")

# a, b, c = map(int, input().split())
# print("대박" if (a+b+c)%1000//100%2==0 else "그럭저럭")

# a, b, c = map(int, input().split())
# if a > 170 and b > 170 and c > 170:
#     print("PASS")
# else:
#     if a <= 170:
#         print("CRASH", a)
#     elif b <= 170:
#         print("CRASH", b)
#     else:
#         print("CRASH", c)

# a = int(input())
# print("양수" if a > 0 else 0 if a ==0 else "음수")

# a, b = map(int, input().split())
# if b>=30:
#     print(a, b-30)
# else:
#     if a-1 >= 0:
#         print(a-1, b+30)
#     else:
#         print(23, b+30)

# a, b = map(int, input().split())
# if b%a == 0: print (f"{a}*{int(b/a)}={b}")
# elif a%b == 0: print(f"{b}*{int(a/b)}={a}")
# else: print("none")

# a, b, c = map(int, input().split())
# if max(a, b, c) == a:
#     print("yes" if a < (b+c) else "no")
# elif max(a, b, c) == b:
#     print("yes" if b < (a+c) else "no")
# else :
#     print("yes" if c < (a+b) else "no")

# a, b = map(int, input().split())
# if a%400 == 0 or (a%4 == 0 and a%100 != 0):
#     if b == 1 or b == 3 or b == 5 or b == 7 or b == 8 or b == 10 or b == 12:
#         print(31)
#     elif b == 4 or b == 6 or b == 9 or b == 11:
#         print(30)
#     else :
#         print(29)
# else :
#     if b == 1 or b == 3 or b == 5 or b == 7 or b == 8 or b == 10 or b == 12:
#         print(31)
#     elif b == 4 or b == 6 or b == 9 or b == 11:
#         print(30)
#     else :
#         print(28)