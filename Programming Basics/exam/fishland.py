mackerel_price = float(input())  # скумрия
sprat_price = float(input())  # цаца
palamud_kg = float(input()) # паламуд
horse_mackerel_kg = float(input()) # сафрид
mussel_kg = int(input())

palamud_price = 1.6 * mackerel_price
horse_mackerel_price = 1.8 * sprat_price
mussel_price = 7.5

amount = palamud_kg * palamud_price + horse_mackerel_kg * horse_mackerel_price + mussel_kg * mussel_price

print('%.2f' %amount)
