from math import floor

needed_working_hours = int(input())
days = int(input())
employees = int(input())

days *= 0.9
extra_worked_hours = employees * days * 2
real_worked_hours = floor(days * 8 * employees + extra_worked_hours)

if real_worked_hours >= needed_working_hours:
    print(f'Yes!{real_worked_hours - needed_working_hours} hours left.')
else:
    print(f'Not enough time!{needed_working_hours - real_worked_hours} hours needed.')