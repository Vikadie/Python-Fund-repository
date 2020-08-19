capacity = int(input()) # capacity of possible messages kept at once per user

commands = input()

d = dict()
while commands != 'Statistics':
    command, *args = commands.split('=')
    if command == 'Add':
        username, sent, received = args
        if username not in d:
            d[username] = [int(sent), int(received)]
    elif command == 'Message':
        sender, receiver = args
        if sender in d and receiver in d:
            d[sender][0] += 1
            d[receiver][1] += 1
            if d[sender][0] + d[sender][1] == capacity:
                del d[sender]
                print(f"{sender} reached the capacity!")
            if d[receiver][0] + d[receiver][1] == capacity:
                del d[receiver]
                print(f"{receiver} reached the capacity!")
    elif command == 'Empty':
        if args[0] == 'All':
            d.clear()
        else:
            username = args[0]
            if username in d:
                del d[username]

    commands = input()

print(f"Users count: {len(d)}")

d_ordered = dict(sorted(d.items(), key= lambda x: (-x[1][1], x[0])))

for username, messages in d_ordered.items():
    print(f"{username} - {messages[0] + messages[1]}")