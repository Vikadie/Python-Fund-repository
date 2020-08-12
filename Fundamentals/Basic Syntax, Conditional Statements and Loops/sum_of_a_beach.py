string = input().lower()

list = ["Sand", "Water", "Fish", "Sun" ]
# search for Sun
counter = 0
length = len(string)
for i in range(length - 2):
    if string[i:i+3].capitalize() in list:
        counter += 1
# search for Sand and Fish
for i in range(length - 3):
    if string[i:i+4].capitalize() in list:
        counter += 1
#search for Water
for i in range(length - 4):
    if string[i:i+5].capitalize() in list:
        counter += 1

print(counter)