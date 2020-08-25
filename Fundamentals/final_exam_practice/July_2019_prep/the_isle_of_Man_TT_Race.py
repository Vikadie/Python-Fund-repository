import re

pattern = r'([#\$%\*\&])([A-Za-z]+)\1=(\d+)!!(.+)'

while True:
    line = input()
    if not line:
        break
    x = re.findall(pattern, line)

    if x:
        if int(x[0][2]) == len(x[0][3]):
            geohashcode = ''
            for ch in x[0][3]:
                decr_ch = ord(ch) + int(x[0][2])
                geohashcode += chr(decr_ch)
            print(f"Coordinates found! {x[0][1]} -> {geohashcode}")
            break
        else:
            print(f"Nothing found!")
    else:
        print(f"Nothing found!")
