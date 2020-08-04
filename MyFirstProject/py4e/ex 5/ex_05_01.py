num = 0
tot = 0.0
while True:
    sval = input('Entrer un numéro ou "fin" pour finir:')
    if sval == 'fin':
        break
    try:
        fval = float(sval)
    except:
        print('Saisie invalide')
        continue
    num=num+1
    tot=tot+fval

#print the total of all inserted numbers, the count of the numbers inserted and their average
print('La somme des numéros saisis est: ', tot,'; Les numéros insérés sont:', num,'; La moyenne est:', tot/num)
