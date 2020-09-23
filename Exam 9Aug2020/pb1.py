# World Tour
stops = input()
line = input()

while line != 'Travel':
    command, str1, str2 = line.split(':')
    if command == 'Add Stop':
        index = int(str1)
        if 0 <= index < len(stops):
            stops = stops[:index] + str2 + stops[index:]
    elif command == 'Remove Stop':
        start_index = int(str1)
        end_index = int(str2)
        if (0 <= start_index < len(stops)) and (0 <= end_index < len(stops)):
            stops = stops[: start_index] + stops[end_index + 1:]
    elif command == 'Switch':
        if str1 in stops:
            stops = stops.replace(str1, str2)
    print(stops)

    line = input()

print(f"Ready for world tour! Planned stops: {stops}")