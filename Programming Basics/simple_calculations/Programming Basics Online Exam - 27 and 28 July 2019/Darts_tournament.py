current = int(input())

count = 0

while current > 0:
    sector = input()

    if sector == "bullseye":
        current = "bullseye"
        count += 1
        break

    points = int(input())

    if sector == "number section":
        current = current - points
        count += 1
        continue
    elif sector == "double ring":
        current = current - 2 * points
        count += 1
        continue
    elif sector == "triple ring":
        current = current - 3 * points
        count += 1
        continue

if current == 0:
    print(f"Congratulations! You won the game in {count} moves!")
elif current == "bullseye":
    print(f"Congratulations! You won the game with a bullseye in {count} moves!")
else:
    print(f"Sorry, you lost. Score difference: {-current}.")
