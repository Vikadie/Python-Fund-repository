n_persons = int(input())
capacity_p = int(input())
courses = n_persons // capacity_p
remaining = 1 if n_persons % capacity_p != 0 else 0
print(courses + remaining)