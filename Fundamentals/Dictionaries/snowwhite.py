from collections import Counter

color_name_ph = dict()  # {color: {name : ph} }
d = dict()  # {color_name : ph}
colors = {}
in_line = input()

while in_line != "Once upon a time":
    dwarfName, dwarfHatColor, dwarfPhysics = in_line.split(" <:> ")
    dwarfPhysics = int(dwarfPhysics)

    if (dwarfHatColor, dwarfName) in d:
        if dwarfPhysics > d[dwarfHatColor, dwarfName][0]:
            d[dwarfHatColor, dwarfName] = [dwarfPhysics, dwarfHatColor]
    else:
        colors[dwarfHatColor] = colors.get(dwarfHatColor, 0) + 1
        d[dwarfHatColor, dwarfName] = [dwarfPhysics, dwarfHatColor]

    in_line = input()

d_sorted = dict(sorted(d.items(), key=lambda x: (-x[1][0], -colors[x[1][1]])))

for key, value in d_sorted.items():
    name, [physic, dwarfHatColor] = key[1], value
    print(f"({dwarfHatColor}) {name} <-> {physic}")