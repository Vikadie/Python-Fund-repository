#SoftUni reception
employee_1_efficiency = int(input())
employee_2_efficiency = int(input())
employee_3_efficiency = int(input())

students_count = int(input())

total_efficiency = employee_1_efficiency + employee_2_efficiency + employee_3_efficiency

time = 0
while students_count > 0:
    time += 1
    if time % 4 != 0:
        students_count -= total_efficiency

print(f"Time needed: {time}h.")