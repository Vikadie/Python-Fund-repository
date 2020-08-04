#checkin the python file
print("PY4E")
#start of the exercise
score = input("Enter Score: ")

try :
    S = float(score)
except :
    print("Enter Score between 0 and 1")
    quit()

if S > 1:
    print("Enter Score between 0 and 1")
elif S >= 0.9:
    print("A")
elif S >= 0.8:
    print("B")
elif S >= 0.7:
    print("C")
elif S >= 0.6:
    print("D")
elif S <= 0:
    print("Enter Score between 0 and 1")
elif S < 0.6:
    print("F")
