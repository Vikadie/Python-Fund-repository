inp = input()

dict_user_result = dict()
language_submissions = dict()

while inp != "exam finished":
    try:
        username, language, points = inp.split('-')
        if username in dict_user_result:
            if int(points) > dict_user_result[username]:
                dict_user_result[username] = int(points)
        else:
            dict_user_result[username] = int(points)
        language_submissions[language] = language_submissions.get(language, 0) + 1
    except ValueError:
        username, banned = inp.split('-')
        if username in dict_user_result:
            dict_user_result.pop(username)

    inp = input()

dict_sorted_results = dict(sorted(dict_user_result.items(), key = lambda x: (-x[1], x[0])))
dict_sorted_languages = dict(sorted(language_submissions.items(), key = lambda x: (-x[1], x[0])))

print("Results:")
for k, v in dict_sorted_results.items():
    print(f"{k} | {v}")
print("Submissions:")
for l, s in dict_sorted_languages.items():
    print(f"{l} - {s}")