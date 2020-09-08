owned_vehicles = input().split(", ")

number_of_commands = int(input())

for command_num in range(1, number_of_commands + 1):
    command, tokens = input().split(", ", 1)
    if command == "Add":
        if tokens in owned_vehicles:
            print("Tank is already bought")
        else:
            print("Tank successfully bought")
            owned_vehicles.append(tokens)
    elif command == "Remove":
        if tokens in owned_vehicles:
            print("Tank successfully sold")
            owned_vehicles.remove(tokens)
        else:
            print("Tank not found")
    elif command == "Remove At":
        index = int(tokens)
        if 0 <= index < len(owned_vehicles):
            del owned_vehicles[index]
            print("Tank successfully sold")
        else:
            print("Index out of range")
    elif command == "Insert":
        index, tank_name = tokens.split(", ")
        index = int(index)
        if 0 <= index < len(owned_vehicles):
            if tank_name in owned_vehicles:
                print("Tank is already bought")
            else:
                owned_vehicles.insert(index, tank_name)
                print("Tank successfully bought")
        else:
            print("Index out of range")


print(", ".join(owned_vehicles))