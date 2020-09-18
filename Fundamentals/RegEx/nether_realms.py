demons = input().split(',')
demons_list = []
for demon in demons:
    demon = demon.strip()
    health = 0
    digit_str = ""
    count_divide = 0
    damage = 0
    for ch in demon:
        if not ch.isdigit() and ch not in ['-', '*', '/', '.', '+']:
            health += ord(ch)
        if ch == '*':
            count_divide += 1
        elif ch == '/':
            count_divide -= 1
        if ch not in ['.'] and not ch.isdigit() and digit_str != "":
            damage += float(digit_str)
            digit_str = ""
        if ch in ['-', '.'] or ch.isdigit():
            digit_str += ch

    if digit_str != "":
        damage += float(digit_str)
        digit_str = ""
    for _ in range(abs(count_divide)):
        if count_divide > 0:
            damage *= 2
        elif count_divide < 0:
            damage /= 2

    demon_str = f"{demon} - {health} health, {damage:.2f} damage"
    demons_list.append(demon_str)

for d in sorted(demons_list):
    print(d)
