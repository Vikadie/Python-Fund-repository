electrons = int(input())

electron_distribution_list = []
shield_index = 1
while(electrons > 0):
    electrons_to_distribute = 2 * shield_index ** 2
    if electrons >= electrons_to_distribute:
        electrons -= electrons_to_distribute
        electron_distribution_list.append(electrons_to_distribute)
    else:
        electron_distribution_list.append(electrons)
        electrons = 0
    shield_index += 1

print(electron_distribution_list)