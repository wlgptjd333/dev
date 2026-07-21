# 문제 16. 학생 성적 분석
# 학생의 국어, 영어, 수학 점수를 입력받아 리스트에 저장하세요.
#
# 그리고 다음 결과를 출력하세요.
#
# - 점수 리스트
# - 총점
# - 평균
# - 평균이 60점 이상인지
# - 모든 과목이 40점 이상인지
#
# 예:
#
# ```
# 국어: 80
# 영어: 70
# 수학: 50
#
# 점수: [80, 70, 50]
# 총점: 200
# 평균: 66.66666666666667
# 평균 60점 이상: True
# 모든 과목 40점 이상: True
# ```

kr = int(input("국어: "))
en = int(input("영어: "))
mt = int(input("수학: "))
scorelist = [kr, en, mt]
totalscore = sum(scorelist)
avgscore = totalscore/len(scorelist)

print(f"총점: {totalscore}\n평균: {avgscore}\n평균 60점 이상: {avgscore>=60}\n"
      f"모든 과목 40점 이상: {all(n >= 40 for n in scorelist)}")
