number = int(input())


def perfect_number_check(num):
    sums = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            sums += i
    return sums == num


if perfect_number_check(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
