participants_list = input().split(", ")

line = input()
d = dict()
while line != "end of race":
    name = ""
    distance = 0
    for ch in line:
        if ch.isalpha():
            name += ch
        elif ch.isdigit():
            distance += int(ch)

    if name in participants_list:
        d[name] = d.get(name, 0) + distance

    line = input()

d_sorted = dict(sorted(d.items(), key = lambda x: -x[1]))

names = list(d_sorted.keys())
print(f"1st place: {names[0]}\n2nd place: {names[1]}\n3rd place: {names[2]}")