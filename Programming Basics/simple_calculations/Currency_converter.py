a = float(input("Amount: "))
from_currency = str(input("Enter the currency: "))
to_currency = str(input("to be converted to (currency): "))

if from_currency == "BGN":
    x = a
elif from_currency == "USD":
    x = a * 1.79549
elif from_currency == "EUR":
    x = a * 1.95583
elif from_currency == "GBP":
    x = a * 2.53405
else:
    print("You have put currency that the converter cannot recognize. Please, try again and restart the converter!")

if to_currency == "BGN":
    x = x
elif to_currency == "USD":
    x = x / 1.79549
elif to_currency == "EUR":
    x = x / 1.95583
elif to_currency == "GBP":
    x = x / 2.53405
else:
    print("You have put currency that the converter cannot recognize. Please, try again and restart the converter!")

print("%.2f %s" %(x, to_currency))