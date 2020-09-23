gibberish = input()

counter = set()
temp = ""
result = ""
index = -1
num_txt = ""
for char in gibberish:
    index += 1
    if char.isdigit():
        num_txt += char
        if index < len(gibberish) - 1 and gibberish[index + 1].isdigit():
            continue
        num = int(num_txt)
        result += (temp * num)
        temp = ""
        num_txt = ""
    else:
        char = char.upper()
        temp += char

print(f"Unique symbols used: {len(set(result))}")
print(result)