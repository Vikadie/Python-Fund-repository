import re

n = int(input())

pattern = r'([\*@])([A-Z][a-z]{2,})\1:\s((\[([A-Za-z])\]\|){3})$'

for _ in range(n):
    msg = input()

    x = re.findall(pattern, msg)
    encrypted_list = []
    if x:
        for letter in x[0][2]:
            if letter.isalpha():
                encrypted_list.append(str(ord(letter)))
        print(f"{x[0][1]}: {' '.join(encrypted_list)}")
    else:
        print("Valid message not found!")