import re
n = int(input())

for _ in range(n):

    message = input()

    pattern = r'!([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})\]'

    x = re.findall(pattern, message)

    command =""
    msg = []
    if x:
        command = x[0][0]
        msg = [str(ord(ch)) for ch in x[0][1]]
        print(f"{command}: {' '.join(msg)}")
    else:
        print("The message is invalid")