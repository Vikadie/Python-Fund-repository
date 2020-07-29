book_name = input()
library_capacity = int(input())
current_check = 0
found_it = False
while current_check < library_capacity:
    check_name = input()
    if check_name == book_name:
        found_it = True
        break
    current_check += 1

if found_it:
    print(f'You checked {current_check} books and found it.')
else:
    print(f'The book you search is not here!\nYou checked {current_check} books.')