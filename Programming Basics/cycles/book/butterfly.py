import math

n = int(input())

width = 2 * n - 1
wing_width = n - 1
height = 2 * (n-2) + 1

mid = ' ' * wing_width + '@' + ' '* wing_width
for i in range(height):

    if (i + 1) % 2 != 0:
        upper_wings = '*' * (wing_width - 1) + '\\' + ' ' + '/' + '*' * (wing_width - 1)
        bottom_wings = '*' * (wing_width - 1) + '/' + ' ' + '\\' + '*' * (wing_width - 1)
    else:
        upper_wings = '-' * (wing_width - 1) + '\\' + ' ' + '/' + '-' * (wing_width - 1)
        bottom_wings = '-' * (wing_width - 1) + '/' + ' ' + '\\' + '-' * (wing_width - 1)

    if (i + 1) < math.floor(height / 2) + height % 2:
        print(upper_wings)
    elif (i + 1) == math.floor(height / 2) + height % 2:
        print(mid)
    else:
        print(bottom_wings)


