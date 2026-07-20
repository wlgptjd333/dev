#변수에 대해 더 배우기
#동적 타이핑

'''
변수 명명 규칙
문자, 숫자, _
숫자로 시작 X
대소문자 구분
예약어 X
#if, for, True, class
의미 있게
snake_case 언더스코어 이용해서 띄어쓰기 표기
camelCase 낙타 등처럼 대소문자로 표기
상수 TOTAL_PRICE
'''

x,y = 10, 20
print(x,y)
'''
10, 20 묶어놓음 => 튜플
temp = 10, 20   튜플을 만들고 그 값을 넣어주는 것과 마찬가지다.
x, y = temp
'''

x="123"
print(type(x)) #문자열
x = int(x)
print(type(x)) #정수

del x   # 변수 삭제
print(x)