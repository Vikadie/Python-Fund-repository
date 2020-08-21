income = float(input())
months = int(input())
private_expenses = float(input())

# exit: She can save {максимален процент от дохода си, който може да спести}
# {сумата, която ще успее да спести}

saving = (income - private_expenses - 0.3 * income)
monthly_savings = months * saving

print(f'She can save {(100 * saving / income):.2f}%')
print(f'{monthly_savings:.2f}')
