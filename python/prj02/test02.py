#자료구조
"""
list :
    - [ ]
    - 순서 O , 수정 O, 중복 O
tuple :
    - ( )
    - 순서 O, 수정 X, 중복 O
dictionary :
    - {key:value}
    - 키-값, 수정 O
set :
    - { }
    - 순서 X, 중복 X
"""

#tuple 1+(2+3)같은 우선순위 괄호랑 잘 구분하기
# ,콤마가 있어야 튜플로 취급됨.

x = (100,200,300,"사과","바나나")
print(x[0])
print(len(x))
print("사과" in x)
# print(type(x))
