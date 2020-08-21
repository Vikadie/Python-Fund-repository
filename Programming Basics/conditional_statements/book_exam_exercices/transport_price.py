n_km = int(input())
day_period = input() #day or night

price = 0
if n_km < 20: # taxi
    taxi_tariff = 0
    if day_period == "day":
        taxi_tariff = 0.79
    elif day_period == "night":
        taxi_tariff = 0.9
    else:
        print("invalid input")
    price = 0.7 + taxi_tariff * n_km
elif n_km < 100: # bus
    price = 0.09 * n_km
else: # train
    price = 0.06 * n_km

print(price)