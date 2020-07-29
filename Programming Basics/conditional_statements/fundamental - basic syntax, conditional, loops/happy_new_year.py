year = int(input())

while True:
    year +=1
    digits = str(year)
    r = set(map(int, digits))
    if len(r) == len(digits):
        print(year)
        break
