#출력문
#타입
#자료구조

# x = ["엑", "스"]
# y = ["와", "이"]
#
# result = x+y
# print(result)
#
# x[0] = "안녕"
# print(result)
# print(x+y)

# 연산자 테스트

#산술 : + , - , * , / , // , %

#비교 : < , > , <= , >= , == , !=

#논리 : and , or , not
print(not True and True)

# 리스트
# '''
# 100 , 90, 95
# '''
# score_list = []
# score_list.append(int(input("학생 성적 : ")))
# score_list.append(int(input("학생 성적 : ")))
# score_list.append(int(input("학생 성적 : ")))
#
# # 기존 score_list의 값들에 5씩 더해서 새로운 리스트로 덮어씁니다.
# score_list = [score + 5 for score in score_list]
#
# print(score_list)


# 문제1
# 첫번째요소 , 마지막요소 출력
fruits = ["사과", "바나나", "포도", "귤", "감"]
print(fruits[0], fruits[-1])

# 문제2
# 리스트 [10, 20, 30]에 다음을 순서대로 적용
# 1. 맨 끝에 40 추가
# 2. 맨 앞에 5 삽입
# 3. 20 삭제
# 최종 결과 출력 (기대값: [5, 10, 30, 40])
pr2 = [10, 20, 30]
pr2.append(40)
pr2.insert(0, 5)
pr2.remove(20)
print(pr2)

# 문제3
# 리스트 ["김", "이", "박", "이", "최"]에서
# "이"가 몇 번 나오는지 출력하고, "박" 의 위치(인덱스) 출력
pr3 = ["김", "이", "박", "이", "최"]
print(pr3.count("이"))
print(pr3.index("박"))

# 문제4
# 리스트 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]에서 슬라이싱만 사용해 아래를 각각 출력하세요.
# 1. 앞 3개 → [1, 2, 3]
# 2. 뒤 3개 → [8, 9, 10]
# 3. 짝수 인덱스 값만 → [1, 3, 5, 7, 9]
# 4. 전체 역순 → [10, 9, 8, ..., 1]
pr4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(pr4[:3])
print(pr4[-3:])
print(pr4[::2])
print(pr4[::-1])
