number = int(input())

def odd_n_even_sum(n):
    odd = 0
    even = 0
    while n > 0:
        num = n % 10
        if num % 2 == 0:
            even += num
        else:
            odd += num
        n = n//10

    return (odd, even)

odd, even = odd_n_even_sum(number)
print(f"Odd sum = {odd}, Even sum = {even}")