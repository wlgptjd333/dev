# 자료구조 4가지
# list : 순서 O, 변경 O, 중복 O, 다양한 타입
'''
1byte : 256(-128~127)
'''

x = ["사과", "딸기", 3.14, 100, True, "계란", [1,2,3]]
print(x)
print(type(x[6]))
x[0] = "바나나"
print(x[-7:0:-1])      # print(x[begin:end:step])
x[1:3] = ["포도", 9.99, 1,2,3] # 슬라이싱을 이용한 수정
x[1:3] = []     # 슬라이싱을 이용한 삭제
print(x)

x.append(777)
x.insert(2,"홍진호")
x.remove("홍진호")
x.pop(5)
# x.clear()

y = ["박혜린", "박하솔", "이상직", "홍진호", "홍진호"]
x.extend(y)     # 리스트 내의 요소로 추가할 수 있음
print(x)


i = x.index("박하솔")
print(i)

cnt = x.count("홍진호")
print(cnt)

x.reverse()     # 원본을 건드림
print(x)

x2 = x
print(x2)
x[0] = "임요한"
print(x)        # x 에는 주소값이 들어가있음(포인터)
print(x2)
'''
변수=변수 왼쪽과 오른쪽이 다르게 해석됨. 왼쪽은 주소값, 오른쪽은 데이터
'''
# tuple
# dictionary
# set
