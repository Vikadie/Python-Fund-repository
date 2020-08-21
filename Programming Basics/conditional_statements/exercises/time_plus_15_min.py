hour = int(input())
minutes = int(input())

minutes = minutes + 15

if minutes >= 60:
    hour += 1
    if hour == 24:
        hour = 0
    minutes = minutes - 60

if minutes < 10:
    minutes = "0" + str(minutes)

print(f"{hour}:{minutes}")