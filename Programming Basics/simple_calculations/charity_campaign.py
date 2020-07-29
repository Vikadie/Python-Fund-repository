campaign_days = int(input())
number_participants = int(input())
number_cakes_per_participant = int(input())
number_gofreths_per_participant = int(input())
number_pancakes_per_participant = int(input())

# price_cake = 45
# price_gofretг = 5.80
# price_pancake = 3.20
#calculation of income per sweet
in_cakes = 45 * number_cakes_per_participant
in_gofreths = 5.80 * number_gofreths_per_participant
in_pancakes = 3.20 * number_pancakes_per_participant
# collected amount - expenses
amount = (1 - 1/8) * (campaign_days * number_participants) * (in_cakes + in_gofreths + in_pancakes)

print("%.2f" % amount)