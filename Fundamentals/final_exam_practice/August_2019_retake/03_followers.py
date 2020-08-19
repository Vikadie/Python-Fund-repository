line = input()

followers = dict() # : [likes, comments]
while line != 'Log out':
    command, username, *args = line.split(": ")
    if command == 'New follower':
        if username not in followers:
            followers[username] = [0, 0]
    elif command == 'Like':
        if username in followers:
            followers[username][0] += int(args[0])
        else:
            followers[username] = [int(args[0]), 0]
    elif command == 'Comment':
        if username in followers:
            followers[username][1] += 1
        else:
            followers[username] = [0, 1]
    elif command == 'Blocked':
        if username in followers:
            del followers[username]
        else:
            print(f"{username} doesn't exist.")

    line = input()

print(f'{len(followers)} followers')
ordered_followers = dict(sorted(followers.items(), key= lambda x: (-x[1][0], x[0])))
for username, actions in ordered_followers.items():
    print(f"{username}: {sum(actions)}")
