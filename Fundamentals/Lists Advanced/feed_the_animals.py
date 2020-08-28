command = input()

records_area = {}
records_animals = {}
while command != "Last Info":
    order, animal_name, food_or_dailyFoodLimit, area = command.split(":")
    food_or_dailyFoodLimit = int(food_or_dailyFoodLimit)
    if order == "Add":
        if area in records_area.keys():
            records_area[area][animal_name] = records_area[area].get(animal_name, 0) + food_or_dailyFoodLimit
        else:
            records_area.setdefault(area, {animal_name: food_or_dailyFoodLimit})
        # updating the records_animals dictionary with the animal_name key (if not existing) and adding the dailyfood_limit
        # or just updating the dailyfood_limit with additionanl dailyfood_limit
        records_animals[animal_name] = records_animals.get(animal_name, 0) + food_or_dailyFoodLimit
    elif order == "Feed":
        if area in records_area.keys() and animal_name in records_area[area].keys():
            records_area[area][animal_name] -= food_or_dailyFoodLimit
            if records_area[area][animal_name] <= 0:
                print(f"{animal_name} was successfully fed")
                del[records_area[area][animal_name]]
                if not records_area[area]:
                    del[records_area[area]]

        if animal_name in records_animals.keys():
            records_animals[animal_name] -= food_or_dailyFoodLimit
            if records_animals[animal_name] <= 0:
                del[records_animals[animal_name]]


    command = input()


# print(records_animals)
print("Animals:")
new_records_animals = {}
for k, v in records_animals.items():
    new_records_animals[v] = new_records_animals.get(v, []) + [k]
# print("new_records_animals", new_records_animals)
# for animal_name in sorted(records_animals, key = lambda animal_name : records_animals[animal_name], reverse = True):
#     print(f"{animal_name} -> {records_animals[animal_name]}g")
for food in sorted(new_records_animals.keys(), reverse = True):
    for animal in sorted(new_records_animals[food]):
        print(f"{animal} -> {food}g")
# print(records_area)
print("Areas with hungry animals:")
for area in sorted(records_area, key = lambda area: len(records_area[area]), reverse = True):
    print(f"{area} : {len(records_area[area])}")