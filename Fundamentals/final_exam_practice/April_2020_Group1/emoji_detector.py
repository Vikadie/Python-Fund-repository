import re

text = input()

digits = re.findall(r'\d', text)
cool_threshold = 1
for i in digits:
    cool_threshold *= int(i)

pattern = r'(\*{2}([A-Z][a-z]{2,})\*{2})|(::([A-Z][a-z]{2,})::)'

x = re.findall(pattern, text)

to_guard = list()
for i in x:
    word = i[1]
    emoji = i[0]
    if not i[1]:
        word = i[3]
        emoji = i[2]
    ssum = 0
    for ch in word:
        ssum += ord(ch)
    if ssum >= cool_threshold:
        to_guard.append(emoji)

print(f'Cool threshold: {cool_threshold}')
print(f'{len(x)} emojis found in the text. The cool ones are:')
for emoji in to_guard:
    print(emoji)


