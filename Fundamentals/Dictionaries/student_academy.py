n_pairs = int(input())

dict_students = dict()
for _ in range(n_pairs):
    student = input()
    grade = float(input())

    if student in dict_students:
        dict_students[student].append(grade)
    else:
        dict_students[student] = [grade]

filtered_st_dict = dict()
for k, v in dict_students.items():
    av_grade = sum(v) / len(v)
    if av_grade >= 4.5:
        filtered_st_dict[k] = av_grade

output_dict = dict(sorted(filtered_st_dict.items(), key = lambda x: -x[1]))
for k in output_dict.keys():
    print(f"{k} -> {output_dict[k]:.2f}")