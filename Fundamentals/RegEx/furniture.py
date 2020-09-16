import re

line = input()

pattern = "(>>)(?P<furniture>.+)(<{2})(?P<price>\d*\.?\d+)(!)(?P<quantity>\d+)\\b"
ttl_sum = 0
print("Bought furniture:")
while line != "Purchase":
    matches = re.finditer(pattern, line)

    for match in matches:
        if match.group('quantity'):
            ttl_sum +=  int(match.group('quantity')) * float(match.group('price'))
            print(match.group('furniture'))

    line = input()

print(f"Total money spend: {ttl_sum:.2f}")
