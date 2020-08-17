import re

text = input()

pattern = r'(#{1}([A-Za-z]{3,})#{2}([A-Za-z]{3,})#{1})|(@{1}([A-Za-z]{3,})@{2}([A-Za-z]{3,})@{1})'

x = re.finditer(pattern, text)
mirror_words = []
count = 0
for i in x:
    count += 1
    #print(i.groups())
    word1 = i.group(2)
    word2 = i.group(3)
    if not word1:
        word1 = i.group(5)
        word2 = i.group(6)
    if word1 and word1 == word2[::-1]:
        mirror_words.append(f'{word1} <=> {word2}')

if count > 0:
    print(f"{count} word pairs found!")
else:
    print("No word pairs found!")
if not mirror_words:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(', '.join(mirror_words))