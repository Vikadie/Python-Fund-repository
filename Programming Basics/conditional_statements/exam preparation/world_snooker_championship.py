final_type = input()
ticket_type = input()
nr_tickets = int(input())
trophy = input()

if final_type == "Quarter final":
    if ticket_type == "Standard":
        price = 55.5
    elif ticket_type == "Premium":
        price = 105.2
    elif ticket_type == "VIP":
        price = 118.9
    else:
        print("Invalid ticket type!")
elif final_type == "Semi final":
    if ticket_type == "Standard":
        price = 75.88
    elif ticket_type == "Premium":
        price = 125.22
    elif ticket_type == "VIP":
        price = 300.4
    else:
        print("Invalid ticket type!")
elif final_type == "Final":
    if ticket_type == "Standard":
        price = 110.1
    elif ticket_type == "Premium":
        price = 160.66
    elif ticket_type == "VIP":
        price = 400
    else:
        print("Invalid ticket type!")
else:
    print("Invalid input!")

if trophy == "Y":
    photo_price = 40 * nr_tickets
elif trophy == "N":
    photo_price = 0

sum = nr_tickets * price

if sum > 4000:
    sum = 0.75 * sum
elif sum > 2500:
    sum = 0.9 * sum + photo_price
else:
    sum += photo_price

print("%.2f" % sum)