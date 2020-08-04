#name = input("Enter file:")
#if len(name) < 1 : name = "regex_sum_325692.txt" #runs automatically regex_sum_325692.txt, with no need of typing anything
#handle = open(name)
#line = handle.read() # read the whole file as 1 line

#somme = 0 #initialize the final variable
import re #import re

#a = re.findall('[0-9]+', line) #creates a temporary list 'a' with numbers found on the line (file as a line)
#for value in range(len(a)): #for the value of each element (which is string) of the list a
#    num = int(a[value]) #converts it to an integer
#    somme = somme + num #store the sum of the integers up to now in variable somme
#print(somme)

#now short version:
print( sum( [ int(x) for x in re.findall('[0-9]+', open('regex_sum_325692.txt').read()) ] ) )
