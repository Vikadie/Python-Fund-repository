usernames_list = input().split(", ")

for user in usernames_list:
    if 3 <= len(user) <= 16 :
        if "-" in user:
            temp = "".join(user.split("-"))
            if "-" in temp:
                temp = "".join(temp.split("_"))
            if (temp.isalnum()):
                print(user)
        elif "_" in user:
            temp = "".join(user.split("_"))
            if temp.isalnum():
                print(user)
        elif user.isalnum():
            print(user)