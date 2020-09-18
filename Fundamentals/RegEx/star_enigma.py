import re

N = int(input())
pattern = '[star]'
pattern_msg = '(.*)?@(?P<planet>[A-Za-z]+)([^@\-!:>]*):(?P<population>[\d]+)([^@\-!:>]*)!(?P<attack>[AD]{1})!([^@\-!:>]*)->(?P<soldier_count>[\d]+)(.*)?'
attacked_planets = []
destroyed_planets = []
for _ in range(N):
    line = input()
    y = re.findall(pattern, line, flags=re.I)
    x = len(y)
    decoded_msg = ''
    for ch in line:
        decoded_msg += chr(ord(ch) - x)

    y = re.finditer(pattern_msg, decoded_msg)

    for match in y:
        if match.group('attack') == 'D':
            destroyed_planets.append(match.group('planet'))
        elif match.group('attack') == 'A':
            attacked_planets.append(match.group('planet'))

print(f'Attacked planets: {len(attacked_planets)}')
for p in sorted(attacked_planets):
    print(f'-> {p}')
print(f'Destroyed planets: {len(destroyed_planets)}')
for dp in sorted((destroyed_planets)):
    print(f'-> {dp}')

