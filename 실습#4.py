def make_score_list():
    kor_score = [49, 79, 20, 100, 80]
    math_score = [43, 59, 85, 30, 90]
    eng_score = [49, 79, 48, 60, 100]
    midterm_score = [kor_score, math_score, eng_score]
    
    return midterm_score
'''print(make_score_list())'''


data = make_score_list()

def get_total_score(x):
    return sum(data[x])

'''print("국어 총점과 평균 : ", get_total_score(0), get_total_score(0)/5)
print("수학 총점과 평균 : ", get_total_score(1), get_total_score(1)/5)
print("영어 총점과 평균 : ", get_total_score(2), get_total_score(2)/5)'''


student_score = [0, 0, 0, 0, 0]
student_name = ['A', 'B', 'C', 'D', 'E']
i = 0
for subject in data:
    for score in subject:
        student_score[i] += score
        i += 1
    i = 0
else:
    '''print("각 학생의 명부: ", student_name)'''
    a, b, c, d, e = student_score
    student_total = [a, b, c, d, e]
    '''print("각 학생의 총점: ", student_total)'''
    student_average = [a/3, b/3, c/3, d/3, e/3]
    '''print("각 학생의 평균: ", student_average)'''
           

def get_credit(x):
    for i in range(0, 5):
        score_credit = data[x][i]
        if score_credit >= 90: credit = 'A'
        elif score_credit >= 80: credit = 'B'
        elif score_credit >= 70: credit = 'C'
        elif score_credit >= 60: credit = 'D'
        else: credit = 'F'
        print(credit, end = '   ')
'''        
print("국어점수 각 학점 ")
get_credit(0)
print('')
print("수학점수 각 학점 ")
get_credit(1)
print('')
print("영어점수 각 학점 ")
get_credit(2)'''

def print_score():
    print("2차원 리스트", make_score_list())
    print("국어 총점과 평균 : ", get_total_score(0), get_total_score(0)/5)
    print("수학 총점과 평균 : ", get_total_score(1), get_total_score(1)/5)
    print("영어 총점과 평균 : ", get_total_score(2), get_total_score(2)/5)
    print("각 학생의 명부: ", student_name)
    print("각 학생의 총점: ", student_total)
    print("각 학생의 평균: ", student_average)
    print("국어점수 각 학점 ")
    get_credit(0)
    print('')
    print("수학점수 각 학점 ")
    get_credit(1)
    print('')
    print("영어점수 각 학점 ")
    get_credit(2)
    
print_score()