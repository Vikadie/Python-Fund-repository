target_seq = list(map(int, input().split()))
target_index = input()

index_list = []
count = 0
while target_index != "End":
    index = int(target_index)
    if index > len(target_seq) - 1:
        target_index = input()
        continue
    if index in index_list:
        target_index = input()
        continue
    index_list.append(index)
    value = target_seq[index]
    target_seq[index] = -1
    count += 1
    for i in range(len(target_seq)):
        if target_seq[i] == -1:
            continue
        elif target_seq[i] <= value:
            target_seq[i] += value
        else:
            target_seq[i] -= value

    target_index = input()

print(f"Shot targets: {count} -> ", end = "")
for target in target_seq:
    print(target, end=" ")