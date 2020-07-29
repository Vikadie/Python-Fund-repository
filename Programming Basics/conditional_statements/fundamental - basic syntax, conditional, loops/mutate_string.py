string_one = list(input())
string_two = list(input())

for i in range(0, len(string_one)):
    if string_one[i] != string_two[i]:
        string_one[i] = string_two[i]
        print("".join(string_one))