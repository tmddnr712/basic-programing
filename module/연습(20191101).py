from module_A import print_st_name_score
import module_B as B

def print_menu():
    menu = """
    *** 선문대학교 ***
    1. 학생정보 출력
    2. 학생정보 입력
    3. 학생정보 수정
    4. 학생정보 삭제
    5. 학생정보 검색
    6. 총점&평균 계산
    7. 종료
"""
    print(menu)

data_dic = {"홍길동" : 100,
            "김유신" : 90,
            "김철수" : 88,
            "이영희" : 95,
            "최선문" : 89}

while(True):
    print_menu()
    num = int(input("무슨 작업을 하시겠습니까?(번호입력) : "))
    if(num == 1):
        print(print_st_name_score(data_dic))
    elif(num == 2):
        B.input_st_name_score(data_dic)
    elif(num == 3):
        modify_st_score(data_dic)
    elif(num == 4):
        delete_st_score(data_dic)
    elif(num == 5):
        search_st_score(data_dic)
    elif(num == 6):
        calculate_sum_ave(data_dic)
    elif(num == 7):
        break
    else:
        print("다시 입력해주세요")