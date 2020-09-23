import re

string = input()

pattern = r'(=|\/)([A-Z][a-z\sA-Z]{2,})\1'

x = re.findall(pattern, string)

destinations = [i[1] for i in x]

travel_points = 0
for d in destinations:
    travel_points += len(d)

if travel_points == 0:
    print(f"Destinations:")
    print(f"Travel Points: 0")
else:
    print(f"Destinations: {', '.join(destinations)}")
    print(f"Travel Points: {travel_points}")