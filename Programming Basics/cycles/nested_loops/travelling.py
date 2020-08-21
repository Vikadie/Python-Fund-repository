destination = input()
while destination != 'End':
    budget = float(input())
    while budget > 0:
        savings = float(input())
        budget -= savings
    print(f'Going to {destination}!')
    destination = input()
