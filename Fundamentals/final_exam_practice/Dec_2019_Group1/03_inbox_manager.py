line = input()

emails_stats = dict()
while line != 'Statistics':
    commands = line.split('->')
    if commands[0] == 'Add':
        username = commands[1]
        if username in emails_stats:
            print(f"{username} is already registered")
        else:
            emails_stats[username] = []
    elif commands[0] == 'Send':
        username, email = commands[1], commands[2]
        if username in emails_stats:
            emails_stats[username].append(email)
    elif commands[0] == 'Delete':
        username = commands[1]
        if username in emails_stats:
            del emails_stats[username]
        else:
            print(f"{username} not found!")

    line = input()

print(f"Users count: {len(emails_stats)}")

ordered_email_stats = dict(sorted(emails_stats.items(), key=lambda x: (-len(x[1]), x[0])))

for user, mails in ordered_email_stats.items():
    print(f"{user}")
    for email in mails:
        print(f"- {email}")