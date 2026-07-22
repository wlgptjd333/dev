# up down game
import random

answer = random.randint(1, 50)
cnt = 0

while True:
    n = int(input())
    if n == answer:
        cnt += 1
        print("정답입니다!", str(cnt) + "번 만에 맞혔습니다!")
        break
    elif n > answer:
        print("Down!")
        cnt += 1
    else :
        print("Up!")
        cnt += 1
