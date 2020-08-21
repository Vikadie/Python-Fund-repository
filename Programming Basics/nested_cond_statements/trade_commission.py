town = input()
s = float(input())

commission = 0

if town == 'Sofia':
    if 0 <= s <= 500:
        commission = 0.05
    elif 500 <= s <= 1000:
        commission = 0.07
    elif 1000 <= s <= 10000:
        commission = 0.08
    elif s > 10000:
        commission = 0.12
elif town == 'Varna':
    if 0 <= s <= 500:
        commission = 0.045
    elif 500 <= s <= 1000:
        commission = 0.075
    elif 1000 <= s <= 10000:
        commission = 0.1
    elif s > 10000:
        commission = 0.13
elif town == 'Plovdiv':
    if 0 <= s <= 500:
        commission = 0.055
    elif 500 <= s <= 1000:
        commission = 0.08
    elif 1000 <= s <= 10000:
        commission = 0.12
    elif s > 10000:
        commission = 0.145

if s >= 0 and town in ['Sofia', 'Plovdiv', 'Varna']:
    print("%.2f" % (s * commission))
else:
    print('error')