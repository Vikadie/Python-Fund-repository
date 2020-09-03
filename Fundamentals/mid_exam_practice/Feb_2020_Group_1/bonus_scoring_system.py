from math import ceil

students_count = int(input())
lectures_count = int(input())
init_bonus = float(input())

students_list_for_attendance = []
total_bonus = 0

for student in range(students_count):
    count_of_attendence_per_student = int(input())
    total_bonus = ceil(count_of_attendence_per_student / lectures_count * (5 + init_bonus))
    students_list_for_attendance.append((total_bonus, count_of_attendence_per_student))

students_list_for_attendance.sort(reverse = True)
if students_count > 0:
    print(f"Max Bonus: {students_list_for_attendance[0][0]}.")
    print(f"The student has attended {students_list_for_attendance[0][1]} lectures.")
else:
    print(f"Max Bonus: 0.")
    print(f"The student has attended 0 lectures.")
