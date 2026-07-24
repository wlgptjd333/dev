import random
from game.kh import judge_up_down

print("===== UP DOWN =====")

# 정답(랜덤)숫자 준비하기
answer = random.randint(1, 100)

while True:
    # 유저한테 입력 받기
    num = int(input("숫자 : "))

    # 판단하기 및 결과 출력
    result = judge_up_down(answer, num)
    print(result)
    if result == True:
        break