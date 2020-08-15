inp = input()

contest_pass_dict = {}
while inp != "end of contests":
    contest, password = inp.split(':')
    contest_pass_dict[contest] = password

    inp = input()

inp = input()

users_dic = dict() # collect all data per user
while inp != "end of submissions":
    contest, password, username, points = inp.split('=>')

    if contest in contest_pass_dict and contest_pass_dict[contest] == password:
        if username in users_dic:
            if contest in users_dic[username]:
                if users_dic[username][contest] < int(points):
                    users_dic[username][contest] = int(points)
            else:
                users_dic[username][contest] = int(points)
        else:
            contest_dict = dict()  # dict to be inserted in the users_dict
            contest_dict[contest] = int(points)
            users_dic[username] = contest_dict

    inp = input()

max_points = 0
user = ""
for username, dict in users_dic.items():
    total_points = 0
    for points in dict.values():
        total_points += points
    if total_points > max_points:
        max_points = total_points
        user = username

print(f'Best candidate is {user} with total {max_points} points.')
print("Ranking:")
for student in sorted(users_dic.keys()):
    print(student)
    student_notes = users_dic[student]
    dict_sorted = sorted(student_notes.items(), key=lambda x: (-x[1]))
    for x in dict_sorted:
        print(f"#  {x[0]} -> {x[1]}")