numbers = []
for _ in range(3):
    numbers.append(int(input()))


def check_sign(a_list):
    count_neg = 0
    for num in a_list:
        if num == 0:
            return "zero"
        elif num < 0:
            count_neg += 1

    if count_neg % 2 == 0:
        return "positive"
    else:
        return "negative"


print(check_sign(numbers))