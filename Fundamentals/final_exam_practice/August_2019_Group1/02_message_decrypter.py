import re

n = int(input())

pattern = r'^([\$%])([A-Z][a-z]{2,})\1:\s\[(\d+)\]\|\[(\d+)\]\|\[(\d+)\]\|$'

for _ in range(n):
    msg = input()

    x = re.findall(pattern, msg)

    if x:
        tag = x[0][1]
        decryptedMessage = ''
        for i in range(2, 5):
            decryptedMessage += chr(int(x[0][i]))
        print(f"{tag}: {decryptedMessage}")
    else:
        print("Valid message not found!")