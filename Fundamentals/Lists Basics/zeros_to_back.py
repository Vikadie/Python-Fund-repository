input_str = list(map(int, input().split(', ')))

count = 0
while(0 in input_str):
    input_str.remove(0)
    count += 1

for j in range(count):
    input_str.append(0)

print(input_str)