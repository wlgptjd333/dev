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

# set

x = {10,20,30,20,30}
print(x)
print(type(x))

x.add(123)
print(x)

x.add(777)
print(x)

x.remove(777)
print(x)