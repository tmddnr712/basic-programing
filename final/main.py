#팀장: 노승욱 / 2018210083
#팀원: 윤건 / 2019315025, 다니구치 종민 / 2019315060
#설계: 노승욱 / 윤건 / 다니구치 종민
#팀프로젝트주제: 카페주인을 위한 소프트웨어
#작성 년월일: 2019.12.09

from introduce_sell import print_product
from introduce_sell import sell_product
from register_delete import register_product
from register_delete import delete_product
from adjust_sales import adjust_product
from adjust_sales import today_sales

from po.print_operation import print_operation

tea_dic = {"아메리카노" : 2000,
           "카페라떼" : 2500,
           "홍차" : 2500,
           "녹차" : 2500}
today = []

while(True):
    print_operation()
    try:
        num = int(input("무슨 작업을 하시겠습니까?(번호입력) : "))
    except ValueError:
        print("다시 입력해 주세요~!")
    else:
        if(num == 1):
            print_product(tea_dic)
        elif(num == 2):
            sell_product(tea_dic, today)
        elif(num == 3):
           register_product(tea_dic)
        elif(num == 4):
            delete_product(tea_dic)
        elif(num == 5):
            adjust_product(tea_dic)
        elif(num == 6):
            today_sales(tea_dic, today)
        elif(num == 7):
            print("작업이 종료 되었습니다.")
            break
        else:
            print("다시 입력해 주세요~!")