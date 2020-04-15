kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 79, 48, 60, 100]
midterm_score = [kor_score, math_score, eng_score]

student_score = [0, 0, 0, 0, 0]
student_name = ['A', 'B', 'C', 'D', 'E']

kor_total = 0
for kor_point in kor_score:
    kor_total = kor_total + kor_point
print("국어과목 총점과 평균: ", kor_total, kor_total/5)

math_total = 0
for math_point in math_score:
    math_total = math_total + math_point
print("수학과목 총점과 평균: ", math_total, math_total/5)

eng_total = 0
for eng_point in eng_score:
    eng_total = eng_total + eng_point
print("영어과목 총점과 평균: ", eng_total, eng_total/5)

i = 0
for subject in midterm_score:
    for score in subject:
        student_score[i] += score
        i += 1
    i = 0
else:
    print("각 학생의 명부: ", student_name)
    a, b, c, d, e = student_score
    student_total = [a, b, c, d, e]
    print("각 학생의 총점: ", student_total)
    student_average = [a/3, b/3, c/3, d/3, e/3]
    print("각 학생의 평균: ", student_average)
    

print("국어점수 각 학점 ")
for i in range(0, 5):
    kor_score_credit = kor_score[i]
    if kor_score_credit >= 90: kor_credit = 'A'
    elif kor_score_credit >= 80: kor_credit = 'B'
    elif kor_score_credit >= 70: kor_credit = 'C'
    elif kor_score_credit >= 60: kor_credit = 'D'
    else: kor_credit = 'F'
    print(kor_credit, end = '   ')
print("")

print("수학점수 각 학점 ")
for i in range(0, 5):
    math_score_credit = math_score[i]
    if math_score_credit >= 90: math_credit = 'A'
    elif math_score_credit >= 80: math_credit = 'B'
    elif math_score_credit >= 70: math_credit = 'C'
    elif math_score_credit >= 60: math_credit = 'D'
    else: math_credit = 'F'
    print(math_credit,end = '   ')
print("")

print("영어점수 각 학점 ")
for i in range(0, 5):
    eng_score_credit = eng_score[i]
    if eng_score_credit >= 90: eng_credit = 'A'
    elif eng_score_credit >= 80: eng_credit = 'B'
    elif eng_score_credit >= 70: eng_credit = 'C'
    elif eng_score_credit >= 60: eng_credit = 'D'
    else: eng_credit = 'F'
    print(eng_credit,end = '   ')