import re

line = input()

pattern = r'^([A-Z][a-z\'\s]+):([A-Z\s]+)$'

while line != 'end':
    x = re.findall(pattern, line)

    if x:
        key = len(x[0][0])
        encrypted = ''
        for ch in line:
            if ch not in ["'", " "]:
                if ch != ':':
                    enc_ch = ord(ch) + key
                    if (97 <= ord(ch) <= 122) and enc_ch > 122:
                        enc_ch = 96 + enc_ch - 122
                    elif (65 <= ord(ch) <= 90) and enc_ch > 90:
                        enc_ch = 64 + enc_ch - 90
                    encrypted += chr(enc_ch)
                else:
                    encrypted += '@'
            else:
                encrypted += ch
        print(f"Successful encryption: {encrypted}")
    else:
        print("Invalid input!")

    line = input()