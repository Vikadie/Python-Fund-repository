command = input()

count = 0
events = ["coding", "dog", "cat", "movie"]
while(command != "END"):
    if command.lower() in events:
        count += 1
        if command.isupper():
            count += 1
    command = input()

if count > 5:
    print("You need extra sleep")
else:
    print(count)
