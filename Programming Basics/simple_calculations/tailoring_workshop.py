rect_tables_pcs = int(input())
length_rect_tables = float(input())
width_rect_tables = float(input())
# calculation of length and width of rectangular cover
length_rect_cover = length_rect_tables + 0.3 * 2
width_rect_cover = width_rect_tables + 0.3 * 2
# calculation of area of rectangular cover
area_rect_cover = length_rect_cover * width_rect_cover
# side carre is 1/2 the lenght of tables
side_carre = length_rect_tables / 2
#calculation of area of carre
area_carre = side_carre ** 2
# price in usd of both carre and rectangular cover
price_usd_rect_table = rect_tables_pcs * area_rect_cover * 7
price_usd_carre = rect_tables_pcs * area_carre * 9
# total price
price_usd = price_usd_rect_table + price_usd_carre
conv_rate = 1.85

print("%.2f USD" % price_usd )
print("%.2f BGN" % (price_usd * conv_rate))