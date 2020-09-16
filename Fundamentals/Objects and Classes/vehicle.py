class Vehicle:

    def __init__(self, type = "", model = "", price = 0):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money, owner_):
        if money >= self.price and self.owner is None:
            self.owner = owner_
            change = money - self.price
            return f"Successfully bought a {self.type}. Change: {change:.2f}"
        elif self.owner is not None:
            return "Car already sold"
        elif money < self.price:
            return "Sorry, not enough money"

    def sell(self):
        if self.owner:
            self.owner = None
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.type} is on sale: {self.price}"


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
vehicle.buy(15000.30, "Peter")
vehicle.buy(35000.40, "George")
vehicle.buy(31000, "Peko")
toyota = Vehicle("car", "Toyota", 15000.30)
print(vehicle)
print(toyota)
toyota.buy(16000, "Ross")
vehicle.sell()
print(vehicle)
print(toyota)
toyota.sell()
print(toyota)