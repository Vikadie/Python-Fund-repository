employee_1_efficiency = int(input()) # count of people that each of the employee can help per hour
employee_2_efficiency = int(input())
employee_3_efficiency = int(input())
people_count = int(input())

sum_all_employee = employee_1_efficiency + employee_2_efficiency + employee_3_efficiency
time = 0
while people_count > 0:
    time += 1
    if time % 4 != 0 or time == 0:
        people_count -= sum_all_employee


print(f"Time needed: {time}h.")