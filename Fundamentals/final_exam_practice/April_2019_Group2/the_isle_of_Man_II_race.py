import re

pattern = r'(["#\$%\*\&])([A-Za-z]+)\1=(\d+)!!(.+)'

while True:
    entry = input()

    if not entry:
        break

    x = re.findall(pattern, entry)

    if x:
        if int(x[0][2]) == len(x[0][3]):
            decrypted_msg = ""
            for ch in x[0][3]:
                decrypted_ch = ord(ch) + int(x[0][2])
                decrypted_msg += chr(decrypted_ch)
            print(f"Coordinates found! {x[0][1]} -> {decrypted_msg}")
            break
        else:
            print("Nothing found!")
    else:
        print("Nothing found!")