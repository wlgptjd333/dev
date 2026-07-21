# Python 점수와 Java 점수를 입력받으세요.
#
# 다음 조건을 모두 만족해야 통과입니다.
#
# - Python 60점 이상
# - Java 60점 이상
# - 두 과목 평균 70점 이상
#
# 결과를 `True`, `False`로 출력하세요.
#
# ```
# Python 점수: 80
# Java 점수: 70
#
# 통과 여부: True
# ```

score_p = int(input("Python 점수: "))
score_j = int(input("Java 점수: "))

print(f"통과 여부: {score_p>=60 and score_j>=60 and (score_p+score_j)/2>=70}")