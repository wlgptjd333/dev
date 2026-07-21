# 국어, 영어, 수학 점수를 입력받아 총점과 평균을 출력하세요.
# 국어: 80
# 영어: 90
# 수학: 70
# 총점: 240
# 평균: 80.0

kr = int(input("국어 : "))
en = int(input("영어 : "))
mt = int(input("수학 : "))
ta = (kr+en+mt)
print(f"총점: {ta} \n평균: {ta/3}")