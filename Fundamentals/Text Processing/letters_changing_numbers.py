line = input().split()
def get_letter_position(letter):
    if letter.isupper():
        return ord(letter) - 64
    elif letter.islower():
        return ord(letter) - 96


def modify(line_str):
    first = line_str[0]
    num = int(line_str[1:-1])
    last = line_str[-1]
    position_first = get_letter_position(first)
    position_last = get_letter_position(last)
    if first.isupper():
        num /= position_first
    elif first.islower():
        num *= position_first

    if last.isupper():
        num -= position_last
    elif last.islower():
        num += position_last

    return num


ssum = 0
for line_str in line:
    ssum += modify(line_str)
print(f"{ssum:.2f}")