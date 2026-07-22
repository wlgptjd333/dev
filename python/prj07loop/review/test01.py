# 숫자를 입력받고, 홀수인지 짝수인지 판단하는 프로그램


while True:
    num = int(input())
    if num == 0:
        break
    elif num % 2 == 0:
        print("even")
    else:
        print("odd")
