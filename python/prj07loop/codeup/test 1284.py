n = int(input())
num_list = []
if n <= 5:
    print("wrong number")
else:
    for i in range(2, n):
        if n % i == 0 and len(num_list) != 2:
            for j in range(1, i+1):
                if i % j == 0 and len(num_list) !=2:
                    num_list.append(i)
                    break

    if len(num_list) < 2 or (num_list[0] * num_list[1]) != n or num_list[0] == 4 or num_list[1] == 4:
        print("wrong number")
    else:
        print(*num_list)
