#설계자: 노승욱 / 2018210083
#작성 년월일: 2019.12.09

#제품 소개
def print_product(dic):
    for name, price in dic.items():
        print("이름 : %s, 가격 : %d" % (name, price))
        
#제품 판매
def sell_product(dic, today):
    print_product(dic)
    print("주문완료 시 '계산'을 입력해 주세요.")
    total = 0
    while True:
        name = input("어떤 제품을 판매하시겠습니까? : ")
        names = dic.keys()
        prices = dic.get(name)
        if(name in names):
            total += prices
        elif(name == "계산"):
            print("커피의 총 가격은 %d원 입니다" %total)
            today.append(total)
            break
        else:
            print("다시 입력해주세요")
    while True:
        try:
            get_price = int(input("얼마를 받으셨습니까? : "))
        except ValueError:
            print("받은돈에 숫자가 입력되지 않았습니다.")
        else:
            change = get_price - total
            print("거스름돈은 %d원 입니다." %change)
            break