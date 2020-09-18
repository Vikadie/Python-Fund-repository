# import re
#
# demons = input().split(', ')
# demons_list = []
# for demon in demons:
#     health = 0
#     damage = 0
#
#     pattern_string = r'[^\d\*\.\+/-]+'
#     health_str = re.findall(pattern_string, demon)
#     #print(health_str)
#     for ch in ''.join(health_str):
#         health += ord(ch)
#     #print('health', health)
#     pattern_digit = r'-?[\d(\.\d+)?]+'
#     digit_str = re.findall(pattern_digit, demon)
#     #print(digit_str)
#
#     for d in digit_str:
#         damage += float(d)
#
#     pattern_mul = '[*/]'
#     #print(re.findall(pattern_mul, demon))
#     for action in re.findall(pattern_mul, demon):
#         #print("damage", damage)
#         if action == '*':
#             damage *= 2
#         elif action == '/':
#             damage /= 2
#
#     demon_str = f"{demon} - {health} health, {damage:.2f} damage"
#     demons_list.append(demon_str)
#
# for d in sorted(demons_list):
#     print(d)



import re
from collections import defaultdict

health_pattern = r"[^0-9\+\-\*/.]"
damage_pattern = r"(-?(\d|\.?\d)+)|/|\*"
no_whitespace = r"[^, ]+"

text = input()
txt_no_comma = re.findall(no_whitespace, text)

demons_health = defaultdict(int)
demons_damage = defaultdict(float)

for x in txt_no_comma:
    health_match = re.findall(health_pattern, x)
    damage_match = re.finditer(damage_pattern, x)

    for h_match in health_match:
        demons_health[x] += ord(h_match)

    count = 0
    for d_match in list(damage_match):
        char = d_match[0]
        if char == "*":
            count += 1
        elif char == "/":
            count -= 1
        else:
            demons_damage[x] += float(char)

    for _ in range(abs(count)):
        if count > 0:
            demons_damage[x] *= 2
        elif count < 0:
            demons_damage[x] /= 2

sorted_demons = dict(sorted(demons_health.items(), key=lambda x: x[0]))

for demon_name, health_points in sorted_demons.items():
    monster_damage = demons_damage[demon_name]
    print(f"{demon_name} - {health_points} health, {monster_damage:.2f} damage")