import collections

Jos_list = list(map(int, input().split()))
k_places = int(input())

killed_list = []
d = collections.deque(Jos_list)
while True:
    d.rotate(-k_places + 1)
    try:
        killed_list.append(d.popleft())
    except IndexError:
        break

print("[", end="")
for i in range(len(killed_list)-1):
    print(killed_list[i], end=",")
print(killed_list[-1], end="]")