import re
participants_list = input().split(", ")

pattern_string = "[^A-Za-z]"
pattern_digit = "[^\d]"
line = input()
d = {}
while line != "end of race":
    name = ""
    x = re.split(pattern_string, line)
    for l in x:
        name += l
    y = [i for i in re.split(pattern_digit, line) if i != '']
    distance = 0
    for m in y:
        for j in d:
            distance += int(j)

    if name in participants_list:
        d[name] = d.get(name, 0) + distance

    line = input()

d_sorted = dict(sorted(d.items(), key=lambda x: -x[1]))

names = list(d_sorted.keys())
print(f"1st place: {names[0]}\n2nd place: {names[1]}\n3rd place: {names[2]}")