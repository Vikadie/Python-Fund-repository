text = input()

take, skip, string = [], [], ""
count = 0
for i in text:
    try:
        i = int(i)
        if count % 2 == 0:
            take.append(i)
        else:
            skip.append(i)
        count += 1
    except:
        string += i

decrypted_message = ""
current_index = 0
for i, j in zip(take, skip):
    decrypted_message += string[current_index : current_index + i]
    current_index += i + j

print(decrypted_message)