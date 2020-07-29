record = float(input())
distance = float(input())
time_per_m = float(input())

from math import floor

slow_down = 12.5 * floor(distance / 15)
# timing - Ivan's time in s
timing = distance * time_per_m + (slow_down)

if timing < record:
    print(f"Yes, he succeeded! The new world record is {timing:.2f} seconds.")
else:
    print(f"No, he failed! He was {(timing - record):.2f} seconds slower.")