# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

d = dict()
for line in handle:
	line=line.rstrip()
	if not line.startswith('From '): #skipping the lines that doesn't start with "From "
		continue
	a = line.split() #split the lines that start with "From "
	#print(a[5]) #check when the hours are places in the list
	b = a[5].split(':') #split the hours in tuples
	#print(a[5], b) #check the correspondence
	c = b[:1]
	#print(c) # check if the list matches
	for hour in c: # create a dict d woth hours places at 1st 2 positions in list c (b[:1])
		d[hour]=d.get(hour,0)+1

#transform the dictionary 'd' into list 'l'
l=list()
for k,v in d.items():
	oldtup=(k,v)
	l.append(oldtup)
#sort the list 'l'
l = sorted(l, reverse=False)
# print the list
for k,v in l:
	print(k,v)

