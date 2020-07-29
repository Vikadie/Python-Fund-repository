max_unsatisfying_results = int(input())
count_unsatisfying_results = 0
count_exams = 0
sum_exams_result = 0
while count_unsatisfying_results < max_unsatisfying_results:
    exam_name = input()
    if exam_name == 'Enough':
        print(f'Average score: {(sum_exams_result / count_exams):.2f}')
        print(f'Number of problems: {count_exams}')
        print(f'Last problem: {last_exam_name}')
        break
    last_exam_name = exam_name
    count_exams += 1
    exam_result = int(input())
    sum_exams_result += exam_result
    if exam_result <= 4:
        count_unsatisfying_results += 1

if count_unsatisfying_results == max_unsatisfying_results:
    print(f'You need a break, {count_unsatisfying_results} poor grades.')