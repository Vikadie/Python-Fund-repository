def program(inp, num):
    if inp == 'int':
        return int(num) * 2
    elif inp == 'real':
        return (f"{(float(num) * 1.5):.2f}")
    elif inp == 'string':
        return (f"${num}$")

i, t = input(), input()
print(program(i, t))