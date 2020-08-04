name = input("Enter file:")
if len(name) < 1 : name = "regex_sum_325692.txt" #runs automatically regex_sum_325692.txt, with no need of typing anything
handle = open(name)

somme = 0 #initialize the final variable
import re #import re

for line in handle:
    line.rstrip() #not really needed but still...
    if re.search('[0-9]+', line):
        a = re.findall('[0-9]+', line) #creates a temporary list 'a' with numbers found on the line for this iteration
        for value in range(len(a)): #for the value of each element (which is string) of the list a
            num = int(a[value]) #converts it to an integer
            somme = somme + num #store the sum of the integers up to now in variable somme
print(somme)
