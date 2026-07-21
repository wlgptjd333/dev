# 숫자 하나 받아서, 양수 음수 zero 판단하기

num1 = int(input("숫자 : "))
if num1 > 0:
    num1_ = "양수"
elif num1 == 0:
    num1_ = "zero"
else:
    num1_ = "음수"
print(num1_)