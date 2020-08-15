sides = dict()

inp = input()

def add_user(force_side, force_user):
    if force_side in sides.keys():
        if force_user not in sides[force_side]:
            sides[force_side].append(force_user)
    else:
        sides[force_side] = [force_user]

while inp != "Lumpawaroo":
    if ' | ' in inp:
        force_side, force_user = inp.split(' | ')
        flag_found_it = False
        for side in sides:
            if force_user in sides[side]:
                flag_found_it = True

        if not flag_found_it:
            add_user(force_side, force_user)

    elif ' -> ' in inp:
        force_user, force_side = inp.split(' -> ')
        flag_found = False
        for side in sides:
            if force_user in sides[side] and side != force_side:
                flag_found = True
                sides[side].remove(force_user)
                add_user(force_side, force_user)
                print(f"{force_user} joins the {force_side} side!")
                break
            elif force_user in sides[side] and side == force_side:
                flag_found = True
                break

        if not flag_found:
            add_user(force_side, force_user)
            print(f"{force_user} joins the {force_side} side!")

    inp = input()

sides = dict(sorted(sides.items(), key = lambda x: (-len(x[1]), x[0]) ))

for k, v in sides.items():
    if len(v) > 0:
        print(f"Side: {k}, Members: {len(v)}")
        for user in sorted(v):
            print(f"! {user}")