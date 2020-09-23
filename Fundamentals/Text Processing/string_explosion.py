string = input()

flag = 0
strength = 0
temp = ""
for i in range(len(string)):
    if not flag:
        if string[i] == '>':
            strength = int(string[i+1])
            flag = 1
        temp += string[i]
    else:
        if string[i] == '>':
            temp += string[i]
            strength += int(string[i+1])
            continue
        elif num == 1:
            flag = 0
            continue
        num -= 1

print(temp)