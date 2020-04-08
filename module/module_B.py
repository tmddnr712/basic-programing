#2 학생정보 입력
def input_st_name_score():
    name = input("이름을 입력해주세요 : ")
    score = input("점수를 입력해주세요 : ")
    dic[name] = score
    
    print(print_st_name_score())

#4 학생정보 삭제
def delete_st_score(dic):
    name = input("누구의 점수를 삭제하시겠습니까 : ")
    names = dic.keys()
    if (name in names):
        dic.pop(name)
    else:
        print("그런 사람은 없습니다.")
        
    print(print_st_name_score())
    
#6 총점&평균 계산
def calculate_sum_ave(dic):
    score = dic.values()
    score_sum = sum(score)
    score_ave = score_sum/len(data_dic)
    print("총점 : %d, 평균 : %d" % (score_sum, score_ave))
    