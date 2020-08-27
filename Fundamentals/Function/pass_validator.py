password = input()


def check_len(s):
    if 6 <= len(s) <= 10:
        return 1
    else:
        return 0


def check_letter_and_digits_only(s):
    if s.isalnum():
        return 1
    else:
        return 0

def at_least_two_digits(s):
    count = 0
    for c in s:
        if c.isdigit():
            count += 1
    if count >= 2:
        return 1
    else:
        return 0


if check_len(password) and check_letter_and_digits_only(password) and at_least_two_digits(password):
    print("Password is valid")
else:
    if not check_len(password):
        print("Password must be between 6 and 10 characters")
    if not check_letter_and_digits_only(password):
        print("Password must consist only of letters and digits")
    if not at_least_two_digits(password):
        print("Password must have at least 2 digits")