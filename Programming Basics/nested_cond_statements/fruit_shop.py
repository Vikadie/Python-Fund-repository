fruit = input()
week_day = input()
quantity = float(input())

price = 0

if week_day in ['Monday', 'Tuesday', "Wednesday", "Thursday", "Friday"]:
    if fruit == "banana":
        price = 2.5
    elif fruit == "apple":
        price = 1.2
    elif fruit == "orange":
        price = 0.85
    elif fruit == "grapefruit":
        price = 1.45
    elif fruit == "kiwi":
        price = 2.7
    elif fruit == "pineapple":
        price = 5.5
    elif fruit == "grapes":
        price = 3.85
    else:
        print("error")
elif week_day in ["Saturday", "Sunday"]:
    if fruit == "banana":
        price = 2.7
    elif fruit == "apple":
        price = 1.25
    elif fruit == "orange":
        price = 0.9
    elif fruit == "grapefruit":
        price = 1.6
    elif fruit == "kiwi":
        price = 3
    elif fruit == "pineapple":
        price = 5.6
    elif fruit == "grapes":
        price = 4.2
    else:
        print("error")
else:
    print("error")

if price != 0:
    final = price * quantity
    print("%.2f" % final)