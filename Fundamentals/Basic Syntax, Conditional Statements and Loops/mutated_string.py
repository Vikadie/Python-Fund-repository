string1 = input()
string2 = input()

for i in range(len(string1)):
    if string2[i] != string1[i]:
        string1 = string2[: i + 1] + string1[i+1 :]
        print(string1)
"""
string1 = input()
string2 = input()
lenght = len(string1)
output1 = ""

j = 0
for i in range(lenght):
    if string2[i] != string1[i]:
        output_list = [(string2[0: i + 1]) + (string1[i + 1: lenght])]
        j = i
        break

for i in range(j, lenght):
    output1 = (string2[0: i + 1]) + (string1[i + 1: lenght])
    if output1 not in output_list:
        output_list.append(output1)
for output in output_list:
    print(output)
"""