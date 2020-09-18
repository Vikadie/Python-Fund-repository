chr1 = input()
chr2 = input()
line = input()

sort_chr = sorted([chr1, chr2])
ssum = 0
for char in line:

    if char > sort_chr[0] and char < sort_chr[1]:
        ssum += ord(char)

print(ssum)