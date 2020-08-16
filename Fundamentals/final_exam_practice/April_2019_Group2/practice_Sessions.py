d = dict()

line = input()

while line != 'END':
    command, *args = line.split('->')
    if command == 'Add':
        road, racer = args
        if road not in d:
            d[road] = [racer]
        else:
            d[road].append(racer)
    elif command == 'Move':
        curr_road, racer, next_road = args
        if racer in d[curr_road]:
            d[curr_road].remove(racer)
            d[next_road].append(racer)
    elif command == 'Close':
        road = args[0]
        if road in d:
            del d[road]

    line = input()

d_ordered = dict(sorted(d.items(), key=lambda x: (-len(x[1]), x[0])))

print("Practice sessions:")
for road, racer_list in d_ordered.items():
    print(road)
    for racer in racer_list:
        print(f"++{racer}")