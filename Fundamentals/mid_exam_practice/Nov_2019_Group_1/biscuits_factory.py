biscuits_per_day_per_worker = int(input())
workers_in_factory = int(input())
competing_factory_biscuits = int(input())

count_biscuits = 0
#calculation for a month - 30 days
for d in range(1, 31):
    produced_biscuits_in_for_day = biscuits_per_day_per_worker * workers_in_factory
    if d % 3 == 0:
        produced_biscuits_in_for_day = int(produced_biscuits_in_for_day * 0.75)
    count_biscuits += produced_biscuits_in_for_day

print(f"You have produced {count_biscuits} biscuits for the past month.")

percentage = abs(100 - 100 * count_biscuits / competing_factory_biscuits)
if count_biscuits > competing_factory_biscuits:
    print(f"You produce {percentage:.2f} percent more biscuits.")
else:
    print(f"You produce {percentage:.2f} percent less biscuits.")
