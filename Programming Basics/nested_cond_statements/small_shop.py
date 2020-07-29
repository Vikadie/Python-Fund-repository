product = input()
city = input()
quantity = float(input())

if product == "coffee":
    if city == "Sofia":
        print(quantity * 0.5)
    elif city == 'Plovdiv':
        print(quantity * 0.4)
    elif city == 'Varna':
        print(quantity * 0.45)
elif product == 'water':
    if city == "Sofia":
        print(quantity * 0.8)
    elif city == 'Plovdiv' or city == 'Varna':
        print(quantity * 0.7)
elif product == 'beer':
    if city == "Sofia":
        print(quantity * 1.2)
    elif city == 'Plovdiv':
        print(quantity * 1.15)
    elif city == 'Varna':
        print(quantity * 1.1)
elif product == 'sweets':
    if city == "Sofia":
        print(quantity * 1.45)
    elif city == 'Plovdiv':
        print(quantity * 1.3)
    elif city == 'Varna':
        print(quantity * 1.35)
elif product == 'peanuts':
    if city == "Sofia":
        print(quantity * 1.6)
    elif city == 'Plovdiv':
        print(quantity * 1.5)
    elif city == 'Varna':
        print(quantity * 1.55)