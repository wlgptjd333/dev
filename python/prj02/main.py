# a = ["카리나", "윈터", "닝닝"]
# b = ("장원영", "안유진", "이서")
#
# print(len(a))
# print(a[0])
# print(a[0:12:3])
#
#
# result = b + ("심원용",)
# print(result)
#
# x = a[0]
# y = a[1]
# z = a[2]
# print(x)
# print(y)
# print(z)
#
# #언패킹: 리스트나 튜플 둘다 가능. 변수명이 내용물보다 많으면 안됨. 변수가 더 적을 경우 *로 몰아넣기 가능.
# # *은 하나만 쓸 수 있음. *로 가져오면 타입은 리스트로 나옴
# *x, y= b
# print(x)
# print(y)
# print(z)
#
# a = (1)
# b = (1,)
# c = ()
# d = 1, 2
# e = ('hello')
#
# print(type(e))
#
#
# students = [('김철수', 85), ('이영희', 92), ('박민수', 78)]
#
# # 1) 모든 학생 이름과 점수를 언패킹으로 출력
# x, y, z = students
# print(x)
# print(y)
# print(z)
# # 2) 모든 학생 이름 출력
# print(x[0], y[0], z[0])
# print(students[0][0], students[1][0], students[2][0])
# # 3) 모든 학생 점수 출력
# print(x[1], y[1], z[1])
# print(students[0][1], students[1][1], students[2][1])

# #집합
# a = {1,2,3}
# b = {2,3,4}
#
# #합집합
# result = a | b
# print(result)
#
# #교집합
# result = a & b
# print(result)
#
# #차집합
# result = a - b
# print(result)
