# loop

# while : 조건식이 참이면 실행하고, 끝나면 처음으로 돌아온다
# 조건식이 거짓이면 실행하지 않는다

num_list = [10,20,30,111,222,333]

i = 0
while i < len(num_list):
    print(num_list[i])
    i += 1

cnt = 0    # 초기식
while cnt < 5:    # 조건식
    print("hello world")
    cnt += 1    # 증감식