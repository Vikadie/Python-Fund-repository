#numbers
input_list = list(map(int, input().split()))

average = sum(input_list)/len(input_list)

output_list = []
for num in input_list:
    if num > average:
        output_list.append(num)

if len(output_list) == 0:
    print("No")
else:
    output = [str(i) for i in sorted(output_list, reverse=True)[: 5]]
    print(' '.join(output))