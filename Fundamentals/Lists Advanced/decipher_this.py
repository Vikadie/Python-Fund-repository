secret_message = input().split()

# message_decoded = []

# for word in secret_message:
#     digit_first_letter = ""
#     string_rest_of_word = ""
#     for i in range(len(word)):
#         if word[i].isdigit():
#             digit_first_letter += word[i]
#         else:
#             string_rest_of_word += word[i:]
#             break
#     first_char = chr(int(digit_first_letter))
#     if len(string_rest_of_word) > 1:
#         rest_of_word = string_rest_of_word[-1] + string_rest_of_word[1: -1] + string_rest_of_word[0]
#     else:
#         rest_of_word = string_rest_of_word
#     message_decoded.append(first_char + rest_of_word)

def parse_to_char(word):
    temp = ""
    for ch in word:
        if not ch.isdigit():
            break
        temp += ch

    ascii_value = int(temp)
    char_value = chr(ascii_value)
    word.replace(temp, char_value)

    return word


def replace_in_word(word):
    temp = list(word)
    temp[1], temp[-1] = temp[-1], temp[1]

    return "".join(temp)


def decript(word):
    res = parse_to_char(word)
    res = replace_in_word(word)

    return res


message_decoded = [decript(word) for word in secret_message]

print(" ".join(message_decoded))

