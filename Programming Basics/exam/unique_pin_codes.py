limit_first_num = int(input())
limit_second_num = int(input())
limit_third_num = int(input())

for P in range(1, limit_first_num + 1):
    for I in range(1, limit_second_num + 1):
        for N in range(1, limit_third_num + 1):
            if P % 2 == 0:
                if I in [2, 3, 5, 7]:
                    if N % 2 == 0:
                        print(P, I, N)