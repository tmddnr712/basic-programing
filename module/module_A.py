# 1번 출력
def print_st_name_score(dic):
    for k, v in data_dic.items():
        print("이름 :",k ,",", "점수 :",v)

# 3번 수정
def modify_st_score(dic):
    name = input("누구를 변경할까요?")
    names = dic.keys()
    if (name in names):
        new_score = int(input("몇 점으로 변경할까요?"))
        dic[name] = new_score
    else:
        print("존재하지 않는 이름입니다!")
    print_st_name_score(dic) # 메뉴 다시 불러오기
    
# 5번 검색
def serach_st_score(dic):
    name = input("누구의 점수를 보시겠습니까?")
    names = dic.keys()
    if (name in names):
        print(name,"학생의 점수는",dic[name],"입니다.")
    else:
        print("존재하지 않는 이름입니다!")
    print_st_name_score(dic) # 메뉴 다시 불러오기