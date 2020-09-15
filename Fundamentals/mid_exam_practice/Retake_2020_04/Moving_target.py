targets_seq = list(map(int, input().split()))
commands = input()

shots = 0
while commands != "End":
    command = commands.split()
    if command[0] == "Shoot":
        index, power = int(command[1]), int(command[2])

        if 0 <= index < len(targets_seq):
            targets_seq[index] -= power
            if targets_seq[index] <= 0:
                shots += 1
                del targets_seq[index]

    elif command[0] == "Add":
        index, value = int(command[1]), int(command[2])

        if 0 <= index < len(targets_seq):
            targets_seq.insert(index, value)
        else:
            print("Invalid placement!")

    elif command[0] == "Strike":
        index, radius = int(command[1]), int(command[2])

        start_index = index - radius
        end_index = index + radius
        if 0 <= start_index < len(targets_seq) and 0 <= end_index < len(targets_seq):
            for i in range(end_index, start_index - 1, -1):
                del targets_seq[i]
        else:
            print("Strike missed!")

    commands = input()

targets_seq_str = [str(i) for i in targets_seq]
print("|".join(targets_seq_str))