n = input()
sum_prime = 0
sum_non_prime = 0

while n != 'stop':
    n = int(n)
    is_non_prime = False
    if n < 0:
        print('Number is negative.')
    else:
        for i in range(2, n):
            if n % i == 0:
                sum_non_prime += n
                is_non_prime = True
                break
        if not is_non_prime:
            sum_prime += n
    n = input()

print(f'Sum of all prime numbers is: {sum_prime}')
print(f'Sum of all non prime numbers is: {sum_non_prime}')