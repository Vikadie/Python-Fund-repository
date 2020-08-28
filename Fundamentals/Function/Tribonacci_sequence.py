num = int(input())

def tribonacci(n):
    lst = []
    for i in range(n):
        if i <= 1:
            lst.append(1)
        elif i == 2:
            lst.append(2)
        else:
            lst.append(lst[i-3] + lst[i-2] + lst[i - 1])

    return lst

print(*tribonacci(num))