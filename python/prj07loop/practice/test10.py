# 자판기

menu ='''
======= 자판기 ======
1. 콜라       1500원
2. 사이다      1300원
3. 커피       2000원
4. 잔액조회
0. 종료
====================
'''
money = 10000
콜라 = 1500
사이다 = 1300
커피 = 2000

# 메뉴판 출력
print(menu)

while True:
    # 유저 메뉴 입력받기
    num = int(input("메뉴번호 : "))
    match num:
        case 1:
            if money > 콜라:
                money = money - 콜라
                print(money, "원 남았습니다")
            else:
                print(money, "원 남았습니다. 잔액이 부족합니다")
        case 2:
            if money > 사이다:
                money = money - 사이다
                print(money, "원 남았습니다")
            else:
                print(money, "원 남았습니다. 잔액이 부족합니다")
        case 3:
            if money > 커피:
                money = money - 커피
                print(money, "원 남았습니다")
            else:
                print(money, "원 남았습니다. 잔액이 부족합니다")
        case 4:
            print(money,"원 남았습니다")
        case 0:
            print("프로그램 종료")
            break
        case _:
            print("잘못된 입력입니다")