commands = input()

d = dict() # band_name: [[members], time]
total_time = 0
while commands != 'start of concert':
    command, band_name, token = commands.split('; ')
    if command == 'Add':
        members = token.split(', ')
        if band_name not in d:
            d[band_name] = [list(members), 0]
        else:
            for member in members:
                if member not in d[band_name][0]:
                    d[band_name][0].append(member)
    elif command == 'Play':
        time = int(token)
        total_time += time
        if band_name not in d:
            d[band_name] = [[], time]
        else:
            d[band_name][1] += time

    commands = input()

d_ordered = dict(sorted(d.items(), key=lambda x: (-x[1][1], x[0])))

print(f"Total time: {total_time}")
for band_name, values in d_ordered.items():
    print(f"{band_name} -> {values[1]}")

band_name_last = input()

print(f"{band_name_last}")
for member in d[band_name_last][0]:
    print(f"=> {member}")