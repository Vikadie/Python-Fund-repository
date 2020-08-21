import re

n = int(input())

pattern = r'U\$([A-Z][a-z]{2,})U\$P@\$([A-Za-z]{5,}[\d]+)P@\$'

count_successful_registrations = 0
for _ in range(n):
    registration = input()

    x = re.findall(pattern, registration)

    if x:
        print("Registration was successful")
        print(f"Username: {x[0][0]}, Password: {x[0][1]}")
        count_successful_registrations += 1
    else:
        print("Invalid username or password")

print(f"Successful registrations: {count_successful_registrations}")