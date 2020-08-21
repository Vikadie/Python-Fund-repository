lenght = int(input())/10
width = int(input())/10
height = int(input())/10
perc_vol_taken = float(input())/100
tot_volume = lenght * width * height
l_to_fill = (1-perc_vol_taken) * tot_volume
print(f"{l_to_fill:.3f}")