capacity = 255
n_lines = int(input())

for i in range(n_lines):
    pour_in = int(input())
    if (capacity - pour_in >= 0):
        capacity -= pour_in
    else:
        print("Insufficient capacity!")
        continue

print(f"{255 - capacity}")