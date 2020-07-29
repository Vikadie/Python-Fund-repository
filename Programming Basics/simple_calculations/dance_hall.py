import math

L = float(input())
W = float(input())
A_wardrobe_side = float(input())

# calculation area of dance hall and free area (area dancing hall - area wardrobe - 10% for the bank)
area = L * W
free_space_area_cm = (area - A_wardrobe_side ** 2 - 0.1 * area) * 100 * 100

# space required by a dancer 40cm2 + 7000 cm2
space_per_dancer = 7040

# print the calculation of the dancers (floored)
print(math.floor(free_space_area_cm/space_per_dancer))