array = list(map(int, input().split()))


def first_last(e_o, count, arr):
    first_last_arr = []
    if e_o == 'even':
        for i in arr:
            if len(first_last_arr) == count:
                return first_last_arr
            if i % 2 == 0:
                first_last_arr.append(i)
    elif e_o == 'odd':
        for i in arr:
            if len(first_last_arr) == count:
                return first_last_arr
            if i % 2 == 1:
                first_last_arr.append(i)
    return first_last_arr


def max_min(order_0, e_o):
    ind = -1
    if order_0 == 'max':
        max = -1001
        for i, n in enumerate(array):
            if e_o == 'even' and n % 2 == 0 and n >= max:
                max = n
                ind = i
            elif e_o == 'odd' and n % 2 == 1 and n >= max:
                max = n
                ind = i
        if ind + 1:
            return ind
        else:
            return "No matches"
    elif order_0 == 'min':
        min = 1001
        for i, n in enumerate(array):
            if e_o == 'even' and n % 2 == 0 and n <= min:
                min = n
                ind = i
            elif e_o == 'odd' and n % 2 == 1 and n <= min:
                min = n
                ind = i
        if ind + 1:
            return ind
        else:
            return "No matches"


command = input()

while command != 'end':
    order = command.split()
    if order[0] == 'exchange':
        index = int(order[1])
        if index >= len(array) or index < 0:
            print("Invalid index")
        else:
            array = array[index + 1:] + array[: index + 1]
    elif len(order) <= 2:
        print(max_min(order[0], order[-1]))
    else:
        count = int(order[1])
        if count > len(array):
            print("Invalid count")
        else:
            if order[0] == 'first':
                print(first_last(order[2], count, array))
            elif order[0] == 'last':
                print(first_last(order[2], count, array[::-1])[::-1])
    command = input()

print(array)