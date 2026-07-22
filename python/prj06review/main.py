# h, w = map(float, input().split())
# w1 = (h - 100) * 0.9
# bmi = (w - w1) * 100 / w1
# print("비만" if bmi >20 else "과체중" if 20 >= bmi > 10 else "정상")

h, w = map(float, input().split())

if h < 150 :
    w1 = (h - 100)
elif h <= 160 :
    w1 = (h - 150) / 2 + 50
else :
    w1 = (h - 100) * 0.9

bmi = (w - w1) * 100 / w1

print("비만" if bmi > 20 else "과체중" if 20 >= bmi > 10 else "정상")
print(bmi)