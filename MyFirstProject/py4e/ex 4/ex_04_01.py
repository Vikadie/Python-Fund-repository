def computepay(h,r) :
    if h > 40.0 :
        pay = (h*r+(h-40)*r*0.5)
    else :
        pay = (h*r)
    return pay

hrs = input("Enter Hours:")
rph = input("Enter rate per hour:")
try :
    h = float(hrs)
    r = float(rph)
except :
    print ("Enter numerical number!")
    quit()

p = computepay(h,r)
print(p)
