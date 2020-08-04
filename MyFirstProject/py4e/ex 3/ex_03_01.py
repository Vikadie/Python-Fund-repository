#checkin the python file
print("PY4E")
hrs = input("Enter Hours:")
rph = input("Enter rate per hour:")
try:
    h = float(hrs)
    rph = float(rph)
except:
    print("Enter numerical numbers!")
    quit()
    
if h <= 40.0:
    print(h*rph)
else:
    print(h*rph+(h-40)*rph*0.5)
#end of the program
