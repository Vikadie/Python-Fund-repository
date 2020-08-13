key = int(input())
n = int(input())

message = []
for i in range(n):
    character = input()
    message.append(chr(ord(character) + key))

for m in message:
    print(m, end="")
