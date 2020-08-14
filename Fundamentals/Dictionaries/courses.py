courses = input()

d = dict()
while courses != 'end':
    course_name, student_name = courses.split(' : ')
    if course_name in d:
        d[course_name].append(student_name)
    else:
        d[course_name] = [student_name]

    courses = input()

d_sorted = dict(sorted(d.items(), key = lambda x: len(x[1]), reverse = True))
for k, v in d_sorted.items():
    print(f"{k}: {len(v)}")
    for student_name in sorted(v):
        print(f"-- {student_name}")
