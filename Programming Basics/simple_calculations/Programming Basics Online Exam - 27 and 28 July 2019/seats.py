T = int(input())
a = []
for _ in range(T):
    a.append(input().strip())

for i in a:
    if len(i) < 5:
        if i.isupper():
            i = i[:3]
        else:
            i = i[3] + i[1] + i[2]
    else:
        i = i[0] + str(ord(i[1]))
    print("Seat decoded:", i)
