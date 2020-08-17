number_of_cars = int(input())

d = dict()

for _ in range(number_of_cars):
    car, mileage, fuel = input().split('|')
    d[car] = [int(mileage), int(fuel)]

command = input()

while command != 'Stop':
    command = command.split(' : ')
    if command[0] == 'Drive':
        car, distance, fuel = command[1], int(command[2]), int(command[3])
        if car in d:
            if d[car][1] >= fuel:
                d[car][0] += distance
                d[car][1] -= fuel
                print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
                if d[car][0] >= 100000:
                    print(f"Time to sell the {car}!")
                    del d[car]
            else:
                print('Not enough fuel to make that ride')
    elif command[0] == 'Refuel':
        car, fuel = command[1], int(command[2])
        if car in d:
            if d[car][1] + fuel <= 75:
                d[car][1] += fuel
            else:
                fuel = 75 - d[car][1]
                d[car][1] = 75
            print(f"{car} refueled with {fuel} liters")
    elif command[0] == 'Revert':
        car, kilometers = command[1], int(command[2])
        if car in d:
            if d[car][0] - kilometers >= 10000:
                d[car][0] -= kilometers
                print(f"{car} mileage decreased by {kilometers} kilometers")
            else:
                d[car][0] = 10000

    command = input()

d_sorted = dict(sorted(d.items(), key = lambda x: (-x[1][0], x[0])))

for car, data in d_sorted.items():
    print(f"{car} -> Mileage: {data[0]} kms, Fuel in the tank: {data[1]} lt.")