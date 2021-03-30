# 밥 무러 간다
# 메뉴 1, 2, 3 아무거나 정해서 
# 먹는 메뉴를 선택 해서 메뉴를 출력
import random
### 아래 문장 전체 반복 ###
for i in range(1,4):

    print("식사메뉴 결정")
    # 메뉴 변수 나열
    menulist = '학식', '분식', '중식'
    print("1. 학식 2. 분식 3. 중식 4. 랜덤 ")
    menu = input(str(i) + " . 입력값 : ")

# 만약에 사용자 입력 값이 1과 같으면
    if menu == "1":
        print("학식 먹어라")
    if menu == "2":
        print("분식 먹어라")
    if menu == "3":
        print("중식 먹어라")
    if menu == "4":
        print(random.choice(menulist))
    
    # 랜덤을 고르면 위 메뉴중에서 아무거나 
    


### 반복 종료 ###
# 커밋 집에서 저장
