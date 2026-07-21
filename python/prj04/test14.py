 # 문제 14. 입력받아 리스트 만들기
 #
 #    사용자로부터 좋아하는 음식 3개를 각각 입력받아 리스트에 저장하세요.
 #
 #    ```
 #    음식1: 치킨
 #    음식2: 피자
 #    음식3: 햄버거
 #    ```
 #
 #    출력:

food1 = input("음식1: ")
food2 = input("음식2: ")
food3 = input("음식3: ")
foodlist = [food1, food2, food3]

print(f"{foodlist}")