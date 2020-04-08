from module_A import print_st_name_score as print_st # 실행 완료 후 메뉴를 표시하기 위해 module_A 의 함수를 import 함

#3 수정
def modify_st_score(dic):
    name = input("누구의 점수를 수정하시겠습니까? : ")
    names = dic.keys()
    if(name in names):
        score = eval(input("몇점으로 수정하시겠습니까? : "))
        dic[name] = score
    else:
        print("존재하지 않는 학생입니다.")
    print_st(dic) # formal parameter 이기 때문에 dic을 받아와야함

#4 삭제
def delete_st_score(dic):
    name = input("누구를 삭제할까요? : ")
    names = dic.keys()
    if(name in names):
        dic.pop(name)
    else:
        print("존재하지 않는 학생입니다.")
    print_st(dic) # formal parameter 이기 때문에 dic을 받아와야함