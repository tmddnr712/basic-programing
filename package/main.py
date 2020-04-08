from module_A import print_st_name_score as print_st
from module_A import input_st_name_score as input_st
from module_B import modify_st_score as modify_st
from module_B import delete_st_score as delete_st
from module_C import search_st_score as search_st
from module_C import calculate_sum_ave as calculate_s_a

from pm.print_menu import print_menu
    
st_dic = {"홍길동" : 100,
          "김유신" : 90,
          "김철수" : 88,
          "이영희" : 95,
          "최선문" : 89}

while(True):
    print_menu()
    try:
        num = int(input("무엇 작업을 하시겠습니까?(번호입력) : "))
    except ValueError:
        print("없는 작업 입니다.")
    else:
        if(num == 1):
            print_st(st_dic) # actual farameter (실질인자, 실제값을 가진 인자)
        elif(num == 2):
            input_st(st_dic)
        elif(num == 3):
            modify_st(st_dic)
        elif(num == 4):
            delete_st(st_dic)
        elif(num == 5):
            search_st(st_dic)
        elif(num == 6):
            calculate_s_a(st_dic)
        elif(num == 7):
            print("종료되었습니다.")
            break
        else:
            print("다시 입력해 주세요~!")