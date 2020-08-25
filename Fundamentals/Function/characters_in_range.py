char1 = input()
char2 = input()


def calculate_a_str_between_chars(c1, c2):
    start = ord(c1) + 1
    end = ord(c2)

    ans_str = ""
    for i in range(start, end):
       ans_str += chr(i) + " "

    return ans_str


print(calculate_a_str_between_chars(char1, char2))
