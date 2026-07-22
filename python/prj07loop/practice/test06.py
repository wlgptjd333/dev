# 1 ~ 10 중에서 3의 배수 합

n = 10
num = 0
while n > 0 :
    num = num + n if n % 3 == 0 else num
    n -= 1
print(num)