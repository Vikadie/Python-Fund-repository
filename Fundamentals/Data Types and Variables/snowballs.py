N = int(input())

max = 0
for i in range(N):
    snowballSnow = int(input())
    snowballTime = int(input())
    snowballQuality = int(input())

    snowballValue = pow((snowballSnow / snowballTime), snowballQuality)
    if (snowballValue > max):
        max = int(snowballValue)
        max_snowballSnow = snowballSnow
        max_snowballTime = snowballTime
        max_snowballQuality = snowballQuality

print(f"{max_snowballSnow} : {max_snowballTime} = {max} ({max_snowballQuality})")