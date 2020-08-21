number = float(input())
in_metric = input()
dest_metric = input()

if in_metric == "mm":
    number = number / 1000
elif in_metric == "cm":
    number = number / 100

if dest_metric == "mm":
    number = number * 1000
elif dest_metric == "cm":
    number = number * 100

print(f"{number:.3f}")