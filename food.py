# 밥 무러 간다
# 메뉴 1, 2, 3 아무거나 정해서 
# 먹는 메뉴를 선택 해서 메뉴를 출력
### 아래 문장 전체 반복 ###
for i in range(1,4):

    print("식사메뉴 결정")
    print("1. 덮밥 2. 김밥 3. 족발 4. 모르겠다 ")
    menu = input(str(i) + " . 입력값 : ")

# 만약에 사용자 입력 값이 1과 같으면
    if menu == "1":
        print("덮밥")
    if menu == "2":
        print("김밥")
    if menu == "3":
        print("족발")
    if menu == "4":
        print("모르겠다.")
### 반복 종료 ###
