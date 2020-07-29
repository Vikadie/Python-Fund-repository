baklava_price = float(input())
muffin_price = float(input())
kg_shtolen = float(input())
kg_bonbon = float(input())
kg_cookies = int(input())

shtolen_price = 1.6 * baklava_price
bonbon_price = 1.8 * muffin_price
cookies_price = 7.5

shtolens = shtolen_price * kg_shtolen
bonbons = kg_bonbon * bonbon_price
cookies = cookies_price * kg_cookies

sum = shtolens + bonbons + cookies

print("%.2f" % sum)