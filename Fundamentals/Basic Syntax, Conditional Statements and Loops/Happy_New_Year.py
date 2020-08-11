current_year = int(input())


next_year = ""
while True:
    current_year += 1
    next_set = set()
    next_year = str(current_year)
    for digit in next_year:
        next_set.add(digit)
    if len(next_year) == len(next_set):
        break


print(int(next_year))

"""current_year += 1
    next_year = str(current_year)
    for digit in next_year:
        new_str = next_year.replace(digit, "", 1)
        if digit in new_str:
            ok = False
            break
        else:
            ok = True
    if ok: break"""