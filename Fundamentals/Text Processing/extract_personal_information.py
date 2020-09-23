N = int(input())

for _ in range(N):
    line = input()
    # name extraction
    name_index_start = line.index("@") + 1 # start name
    name_index_end = line.index("|") # end name
    name = line[name_index_start: name_index_end]
    # age extraction
    age_index_start = line.index("#") + 1
    age_index_end = line.index("*")
    age = line[age_index_start: age_index_end]

    print(f"{name} is {age} years old.")