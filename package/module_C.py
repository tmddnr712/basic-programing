#5 검색
def search_st_score(dic):
    name = input("누구의 점수를 검색하시겠습니까? : ")
    names = dic.keys()
    if(name in names):
        print("%s 학생의 점수는 %d입니다." %(name, dic.get(name)))
    else:
        print("존재하지 않는 학생입니다.")

#6 합평균
def calculate_sum_ave(dic):
    scores = dic.values()
    total = 0
    average = 0.0
    for value in scores:
        total += value
    average = total / len(scores)
    print("총점 : %d, 평균값 : %d" %(total, average))