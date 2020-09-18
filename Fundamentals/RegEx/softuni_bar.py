import re

line = input()

pattern = '(.+)?(%)(?P<customer>[A-Z][a-z]+)(%)(.+)?' \
          '(<)(?P<product>\w+)(>)(.+)?' \
          '(\|)(?P<quantity>\d+)(\|)' \
          '(\D+)?(?P<price>[\d]+[\.]?[\d]+)(\$)'
y = []
ttl_price = 0
while line != 'end of shift':
    matches = re.finditer(pattern, line)

    for match in matches:
        if match.group('price'):
            income = int(match.group('quantity')) * float(match.group('price'))
            text = f"{match.group('customer')}: {match.group('product')} - " \
                   f"{income:.2f}"
            ttl_price += income
            y.append(text)

    line = input()

for text in y:
    print(text)
print(f'Total income: {ttl_price:.2f}')