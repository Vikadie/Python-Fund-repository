num = int(input())


def bar(num):
    percent = '%' * int(num/10)
    dots = '.' * int(10 - num/10)
    to_print = f"{num}% [{percent}{dots}]"
    return to_print


if 0 <= num < 100:
    print(bar(num))
    print("Still loading...")
else:
    print("100% Complete!")
    print(f"[{'%' * int(num/10)}]")