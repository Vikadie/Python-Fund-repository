sq_m = float(input())
price_per_sq_m = 7.61
discount = 18 / 100
discounted_amount = sq_m * price_per_sq_m * discount
final_price = price_per_sq_m * sq_m - discounted_amount
# The final price is: {крайна цена на услугата} lv.
#  The discount is: {отстъпка} lv.
print(f"The final price is: {final_price:.2f} lv.")
print(f"The discount is: {discounted_amount:.2f} lv.")