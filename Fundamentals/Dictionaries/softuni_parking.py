n = int(input())

register_dict = dict()
for _ in range(n):
    inp = input().split()
    username = inp[1]
    if inp[0] == "register":
        license_plate = inp[2]
        if username in register_dict:
            print(f"ERROR: already registered with plate number {register_dict[username]}")
        else:
            register_dict[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
    else:
        if username in register_dict:
            register_dict.pop(username)
            print(f"{username} unregistered successfully")
        else:
            print(f"ERROR: user {username} not found")

for k, v in register_dict.items():
    print(f"{k} => {v}")
