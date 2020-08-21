res_day = int(input())
res_month = int(input())
arrival_day = int(input())
arrival_month = int(input())
leave_day = int(input())
leave_month = int(input())

nights = leave_day - arrival_day

if res_month < arrival_month:
    cost = (nights * 25) * 0.8
else:
    if (arrival_day - res_day) > 10:
        cost = nights * 25
    else:
        cost = nights * 30

print(f"Your stay from {arrival_day}/{arrival_month} to {leave_day}/{leave_month} will cost {cost:.2f}")
