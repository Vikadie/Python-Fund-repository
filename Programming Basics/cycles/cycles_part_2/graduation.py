student_name = input()

class_level = 1
sum_grade = 0
while class_level <= 12:
    grade = float(input())
    if grade >= 4:
        class_level += 1
        sum_grade += grade

print(f'{student_name} graduated. Average grade: {(sum_grade/12):.2f}')