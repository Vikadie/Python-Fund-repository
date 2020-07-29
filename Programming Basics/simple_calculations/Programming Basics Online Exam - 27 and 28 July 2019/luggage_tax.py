width = int(input())
lenght = int(input())
depth = int(input())
priority_bool = input()

if priority_bool == "true":
    priority = True
else: priority = False

V = width * lenght * depth

if V <= 50: tax = 0
elif 50 < V <= 100:
    if priority: tax = 0
    else: tax = 25
elif 100 < V <= 200:
    if priority: tax = 10
    else: tax = 50
elif 200 < V <= 300:
    if priority: tax = 20
    else: tax = 100

print(f"Luggage tax: {tax:.2f}")