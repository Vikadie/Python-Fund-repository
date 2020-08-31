# You will be given a list of numbers and a string. For each element of the list you have to calculate the sum of its
# digits and take the element, corresponding to that index from the text. If the index is greater than the length of the
# text, start counting from the beginning (so that you always have a valid index). Then you get that element from the text,
# you must remove the character you have taken from it (so for the next index, the text will be with one character less).

nums = input().split()
text = input()


# def calculate_index():
#     for j in nums:
#         sum = 0
#         for n in j:
#             sum += int(n)
#         yield sum
indexes = [sum([int(n) for n in j]) for j in nums]

#indexes = list(calculate_index())

ans = ""
for i in indexes:
    j = i % len(text)
    ans += text[j]
    text = text[:j] + text[j + 1:]

print(ans)