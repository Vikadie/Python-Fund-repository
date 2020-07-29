pr_whiskey  = float(input())
beer_litres = float(input())
wine_litres = float(input())
rakia_litres = float(input())
whiskey_litres = float(input())

pr_rakia = 1/2 * pr_whiskey
pr_wine = (1-0.4) * pr_rakia
pr_beer = (1 - 0.8) * pr_rakia

req_amount = pr_whiskey * whiskey_litres + pr_beer * beer_litres + pr_rakia * rakia_litres + pr_wine * wine_litres

print(f"{req_amount:.2f}")