import re
sentence = input()

word = input()

pattern = fr"\b({word})\b"

x = re.findall(pattern, sentence, re.I)

print(len(x))