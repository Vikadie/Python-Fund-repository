from math import trunc

V = int(input())  # volume of the pool
P1 = int(input())  # debit/h of pipe 1
P2 = int(input())  # debit/h of pipe 2
H = float(input())  # work hours

y = P1 * H
z = P2 * H
x = y + z
q = x - V

if q <= 0:
    print(f'The pool is {trunc(100 * (x / V))}% full. Pipe 1: {trunc(100 * (y / x))}%. Pipe 2: {trunc(100 * (z / x))}%.')
else:
    print(f'For {H} hours the pool overflows with {q} liters.')