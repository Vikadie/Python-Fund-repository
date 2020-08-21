income_per_mo = float(input())
months = int(input())
private_expenses_mo = float(input())
#30% for unpredicted expenses
saving_mo = (1-0.3) * income_per_mo - private_expenses_mo

saving_percent = 100 * saving_mo / income_per_mo
saving_amount = saving_mo * months

print(f"She can save {saving_percent:.2f}%")
print(f"{saving_amount:.2f}")