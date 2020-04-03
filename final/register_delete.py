#설계자: 윤건 / 2019315025
#작성 년월일: 2019.12.06

from introduce_sell import print_product

#제품 등록
def register_product(dic):
    name = input("이름을 입력하세요 : ")
    try:
        price = int(input("가격을 입력하세요 : "))
    except ValueError:
        print("가격에 숫자가 입력되지 않았습니다.")
    else:
        dic.update({name : price})
        print("%s가 등록 되었습니다." %name)
    print_product(dic)
    
#제품 삭제
def delete_product(dic):
    name = input("어떤 제품을 삭제할까요? : ")
    names = dic.keys()
    if name in names:
        dic.pop(name)
        print("%s가 삭제 되었습니다." %name)
    else:
        print("등록되지 않은 제품입니다.")
    print_product(dic)