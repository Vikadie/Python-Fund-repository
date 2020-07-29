from math import floor

leap_or_normal = input()
holidays = int(input())
home = int(input())

total_WE = 48 # WE_in_Sofia + home
# he is is Sofia when not at home
WE_in_sofia = total_WE - home
# possibility to play = 3/4 WE(Saturdays) in Sofia
volley_in_sofia = WE_in_sofia * 3/4
# possibility to play on holidays = 2/3 holidays
volley_on_holiday = holidays * 2/3
# when at home each Sunday volley
volley_in_hometown = home
# total volley calculation
total_volley = volley_in_hometown + volley_in_sofia + volley_on_holiday
# 15% more volley if leap year
if leap_or_normal == 'leap':
    total_volley *= 1.15

answer = floor(total_volley)
print(answer)