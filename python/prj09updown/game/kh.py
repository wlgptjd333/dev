def judge_up_down(answer, num):
    if answer > num:
        print("UP")
    elif answer < num:
        print("DOWN")
    else:
        print("correct !!!")
        return True