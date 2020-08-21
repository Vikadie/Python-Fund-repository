price_for_singer = int(input())
sum = 0
guests = 0
while True:
    group = input()
    if group == "The restaurant is full":
        break
    if int(group) < 5:
        price_per_pers = 100
    else:
        price_per_pers = 70

    sum += price_per_pers * int(group)
    guests += int(group)

if sum < price_for_singer:
    print(f"You have {guests} guests and {sum} leva income, but no singer.")
else:
    print(f"You have {guests} guests and {(sum - price_for_singer)} leva left.")