init_passengers = int(input())
all_stops = int(input())
controllers = 2
stops = 0
passengers = init_passengers
while stops < all_stops:
    passengers_out = int(input())
    passengers_in = int(input())
    stops += 1
    if stops % 2 != 0:
        passengers += (- passengers_out + passengers_in + controllers)
    else:
        passengers += ((- passengers_out + passengers_in - controllers))

print(f'The final number of passengers is : {passengers}')
