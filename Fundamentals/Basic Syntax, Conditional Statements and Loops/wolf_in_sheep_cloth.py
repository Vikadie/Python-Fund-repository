list = input().strip().split(", ")[::-1]

for pos, wolf in enumerate(list):
    if wolf == "wolf":
        if pos == 0:
            print("Please go away and stop eating my sheep")
        else:
            print(f"Oi! Sheep number {pos}! You are about to be eaten by a wolf!")