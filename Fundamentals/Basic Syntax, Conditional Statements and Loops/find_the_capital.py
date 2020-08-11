str = input()

position = []
for num, letter in enumerate(str):
    if letter.isupper():
        position.append(num)
print(position)

