line = input()

for i in range(len(line)):
    ch = line[i]

    if i + 1 == len(line) or ch != line[i+1] :
        print(ch, end="")
        if i + 1 == len(line):
            break