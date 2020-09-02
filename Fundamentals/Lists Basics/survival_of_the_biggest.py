entry_lst = list(map(int, input().split()))
nums_to_remove = int(input())

for n in range(nums_to_remove):
    entry_lst.remove(min(entry_lst))

print(entry_lst)
