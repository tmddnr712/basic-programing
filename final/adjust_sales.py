#설계자: 노승욱 / 2018210083
#작성 년월일: 2019.12.06

from introduce_sell import print_product

#제품 가격 수정
def adjust_product(dic):
    name = input("어떤 제품의 가격을 수정할까요? : ")
    try:
        price = int(input("얼마로 수정할까요? : "))
    except ValueError:
        print("가격에 숫자가 입력되지 않았습니다.")
    else:
        names = dic.keys()
        if(name in names):
            dic[name] = price
            print("%s의 가격이 %d원으로 수정되었습니다." %(name, price))
        else:
            print("등록되지 않은 제품입니다.")
        print_product(dic)
        
#당일 매출
def today_sales(dic, today):
    print("당일 매출은",sum(today),"원입니다.")