budget_singer = int(input())

sum = guests = 0
while True:
    persons_per_group = input()
    if persons_per_group == 'The restaurant is full':
        break
    else:
        persons_per_group = int(persons_per_group)

    if persons_per_group < 5:
        sum += persons_per_group * 100
    else:
        sum += persons_per_group * 70

    guests += persons_per_group

if sum >= budget_singer:
    print(f'You have {guests} guests and {(sum - budget_singer)} leva left.')
else:
    print(f'You have {guests} guests and {sum} leva income, but no singer.')