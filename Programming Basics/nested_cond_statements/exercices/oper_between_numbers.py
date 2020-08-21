N1 = int(input())
N2 = int(input())
operator = input()

if N2 == 0 and (operator == '/' or operator == '%'):
    print(f'Cannot divide {N1} by zero')
else:
    if operator == '+' or operator == '-' or operator == '*':
        if operator == '+':
            result = N1 + N2
        elif operator == '-':
            result = N1 - N2
        elif operator == '*':
            result = N1 * N2
        if result % 2 == 0:
            even_or_odd = 'even'
        else:
            even_or_odd = 'odd'
        print(f'{N1} {operator} {N2} = {result} - {even_or_odd}')
    elif operator == '/':
        print(f'{N1} / {N2} = {(N1 / N2):.2f}')
    elif operator == '%':
        print(f'{N1} % {N2} = {(N1 % N2)}')