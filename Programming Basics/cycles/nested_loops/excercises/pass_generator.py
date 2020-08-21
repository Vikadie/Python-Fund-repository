n = int(input())
l = int(input())

for f in range(1, n):

    for s in range(1, n):

        for t in range(1, l + 1):

            for ff in range(1, l + 1):

                for fff in range(1, n + 1):
                    if fff > s and fff > f:
                        print(f, end="")
                        print(s, end="")
                        print(chr(96 + t), end="")
                        print(chr(96 + ff), end="")
                        print(fff, end=" ")
