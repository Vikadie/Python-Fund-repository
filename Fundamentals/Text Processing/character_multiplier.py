word1, word2 = input().split()

min_length = min(len(word1), len(word2))

ssum = 0
for i in range(min_length):
    ssum += ord(word1[i]) * ord(word2[i])

bigger_word = word1
if len(word2) > min_length:
    bigger_word = word2

for char in bigger_word[min_length :]:
    ssum += ord(char)

print(ssum)