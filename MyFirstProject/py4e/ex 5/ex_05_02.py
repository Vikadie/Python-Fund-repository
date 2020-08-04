#print('PY4E')

#start of the ex 5.2
largest = None
smallest = None
#making a loop to find the largest and the smallest of some imputed numbers
while True:
    #ask for a number or 'done' for an end
    num = input("Enter an integer number or 'done' for and end: ")
    if num == "done" : break
    #convert to an integer or show wrong message and restart
    try :
        n = int(num)
    except :
        print('Invalid input')
        continue
    #find whether n is the smallest
    for value in [n]:
        if smallest is None:
            smallest = value
            break
        elif smallest > value:
            smallest = value
            break
    #find whether n is the largest
    for value in [n]:
        if largest is None:
            largest = value
            break
        elif largest < value:
            largest = value
            break

print("Maximum is", largest)
print('Minimum is', smallest)
