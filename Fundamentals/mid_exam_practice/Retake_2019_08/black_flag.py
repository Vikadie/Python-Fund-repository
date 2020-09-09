days_of_pirating = int(input())
plunder_for_day = int(input())
expected_plunder = float(input())

collected_plunder = 0
for d in range(1, days_of_pirating + 1):
    collected_plunder += plunder_for_day
    if d % 3 == 0:
        collected_plunder += 0.5 * plunder_for_day
    if d % 5 == 0:
        collected_plunder *= 0.7

if collected_plunder >= expected_plunder:
    print(f"Ahoy! {collected_plunder:.2f} plunder gained.")
else:
    print(f"Collected only {(100 * collected_plunder/expected_plunder):.2f}% of the plunder.")

