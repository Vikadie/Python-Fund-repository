entry = input().split(", ")

def check_nums_in_lists_are_palindromes(numbers):

    for num in numbers:
        print(num == num[::-1])

check_nums_in_lists_are_palindromes(entry)