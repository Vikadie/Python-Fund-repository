gifts_lift = input().split()
command = input().split()

while(command[0] + ' ' + command[1] != "No Money"):

    if command[0] == "OutOfStock":
        if command[1] in gifts_lift:
            for i in range(len(gifts_lift)):
                if gifts_lift[i] == command[1]:
                    gifts_lift[i] = "None"

    elif command[0] == "Required":
        if 0 <= int(command[2]) < len(gifts_lift):
            gifts_lift[int(command[2])] = command[1]

    elif command[0] == "JustInCase":
        gifts_lift[-1] = command[1]

    command = input().split()

# print(gifts_lift)
for i in gifts_lift:
    if i != "None":
        print(i, end=" ")