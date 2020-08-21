budget = int(input())

while True:
    decoration = input()
    if decoration == "Stop":
        print(f"Money left: {budget}")
        break

    sum = 0

    for letter in decoration:
        sum += ord(letter)

    budget -= sum

    if budget >= 0:
        print(f"Item successfully purchased!")
    else:
        print(f"Not enough money!")
        break

