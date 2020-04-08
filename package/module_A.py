#1 출력
def print_st_name_score(dic): #formal farameter(형식인자(가상변수))
    for i, j in dic.items():
        print("이름 : %s, 점수 : %d" %(i, j))
        
#2 입력        
def input_st_name_score(dic):
    name = input("이름을 입력하세요 : ")
    score = eval(input("점수를 입력하세요 : "))
    dic.update({name : score})
    print_st_name_score(dic)