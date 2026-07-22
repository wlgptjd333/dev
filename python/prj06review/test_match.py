# match

year = 1999
month = 12

if year%400 == 0 or (year%4 == 0 and year%100 != 0):
    match month:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            print(31)
        case 4 | 6 | 9 | 11:
            print(30)
        case 2:
            print(29)
        case _:
            print("ㄴㄴ")
else :
    match month:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            print(31)
        case 4 | 6 | 9 | 11:
            print(30)
        case 2:
            print(28)
        case _:
            print("ㄴㄴ")