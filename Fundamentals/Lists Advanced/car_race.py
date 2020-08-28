timings = list(map(int, input().split()))


def time_calcul(lst):
    time = 0
    for t in lst:
        if t == 0:
            time -= time * 0.2
        time += t

    return time


len_sides = int(len(timings) / 2)
time_left_car = time_calcul(timings[:len_sides])
time_right_car = time_calcul(timings[-len_sides:][::-1])

if time_left_car < time_right_car:
    print(f"The winner is left with total time: {time_left_car:.1f}")
elif time_left_car > time_right_car:
    print(f"The winner is right with total time: {time_right_car:.1f}")