radius = float(input("Enter the radius of the circle in cm r = "))

from math import pi

area = pi * radius ** 2
perimeter = 2 * pi * radius

print(f"Area of the circle is {area:.2f} cm", end=". ")
print(f"Perimeter of the circle is {perimeter:.2f} cm", end=".")