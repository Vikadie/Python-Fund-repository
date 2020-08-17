import re

num = int(input())
for _ in range(num):
    line = input()

    pattern = r'@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@'

    x = re.findall(pattern, line)
    if x:
        bar_code = x[0]
    else:
        print("Invalid barcode")
        continue

    pattern_digit = r'\d'

    y = re.findall(pattern_digit, bar_code)

    code_group = ''
    if y :
        for i in y:
            code_group += i
    else:
        code_group = '00'

    print(f"Product group: {code_group}")