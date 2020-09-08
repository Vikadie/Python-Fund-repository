friend_list = input().split(', ')

commands = input()
while commands != "Report":
    command, indexes = commands.split(' ', 1)
    if command == "Blacklist":
        if indexes in friend_list:
            friend_list[friend_list.index(indexes)] = "Blacklisted"
            print(f"{indexes} was blacklisted.")
        else:
            print(f"{indexes} was not found." )
    elif command == "Error":
        index = int(indexes)
        if 0 <= index < len(friend_list) and (friend_list[index] != "Blacklisted" and friend_list[index] != "Lost"):
            print(f"{friend_list[index]} was lost due to an error." )
            friend_list[index] = "Lost"
    elif command == "Change":
        index, new_name = indexes.split()
        index = int(index)
        if 0 <= index < len(friend_list):
            print(f"{friend_list[index]} changed his username to {new_name}.")
            friend_list[index] = new_name

    commands = input()

print("Blacklisted names:", friend_list.count("Blacklisted"))
print("Lost names:", friend_list.count("Lost"))
print(' '.join(friend_list))