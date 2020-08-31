rooms = int(input())

chairs_ok = 1
ttl_free_chairs = 0
for number_of_room in range(1, rooms + 1):
    chairs, taken = input().split()
    free_chairs = len(chairs) - int(taken)
    if free_chairs < 0:
        print(f"{abs(free_chairs)} more chairs needed in room {number_of_room}")
        chairs_ok = 0
    else:
        ttl_free_chairs += free_chairs

if chairs_ok:
    print(f"Game On, {ttl_free_chairs} free chairs left")
