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

#dictionary : 반드시 기억할 내용 => {}중괄호로 이루어져 있고 키와 밸류로 이루어져 있다.

x = {"name":"홍길동", "age":20, "blood":"A"}
# x["name"] = "홍길동"
# x["age"] = 20
print(x)
print(type(x))
x["age"] = 30
del x["age"]
print(x)
print("age" in x)