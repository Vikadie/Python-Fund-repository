student_name = input()
chk = 0
class_level = 1
sum_grade = 0
while class_level <= 12:
    grade = float(input())
    if grade >= 4:
        class_level += 1
        sum_grade += grade
    else:
        if chk == 0:
            chk = 1
        else:
            print(f'{student_name} has been excluded at {class_level} grade')
            break
if class_level > 12:
    print(f'{student_name} graduated. Average grade: {(sum_grade/12):.2f}')