key_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
junk_materials = {}

flag = False
while True:
    materials = input().split()
    for i in range(0, len(materials), 2):
        material = materials[i + 1].lower()
        quantity = int(materials[i])
        if material in key_materials:
            key_materials[material] += quantity
            if key_materials[material] >= 250:

                key_materials[material] -= 250

                flag = True
                if material == 'shards':
                    print("Shadowmourne obtained!")
                elif material == 'fragments':
                    print("Valanyr obtained!")
                else:
                    print("Dragonwrath obtained!")
                break
        else:
            junk_materials[material] = junk_materials.get(material, 0) + quantity

    if flag:
        break

sorted_key_materials = dict(sorted(key_materials.items(), key = lambda x: (-x[1], x[0])))
for k, v in sorted_key_materials.items():
    print(f'{k}: {v}')

sorted_junk_materials_list = sorted(junk_materials) # this creates a list of sorted keys of junk_materials
# or we can use the option: dict(sorted(junk_materials.items(), key = lambda x: x[0]))
# in case we use a list of sorted keys:
for i in sorted_junk_materials_list:
    print(f'{i}: {junk_materials[i]}')