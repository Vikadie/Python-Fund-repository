tabs = int(input())
salary = int(input())

for tab in range(tabs):
    tab_descr = input()
    if tab_descr == 'Facebook':
        salary -= 150
    elif tab_descr == 'Instagram':
        salary -= 100
    elif tab_descr == 'Reddit':
        salary -= 50

    if salary <= 0:
        print('You have lost your salary.')
        break

if salary > 0:
    print(salary)
