# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# Use the file name mbox-short.txt as the file name
while True :
	fname = input("Enter file name: ")
	try:
		fh = open(fname)
		break
	except:
		print("This file doesn't exist. Please try again!")
		quit()
fh = open(fname)
count=0
ss=0
for line in fh:
	if not line.startswith("X-DSPAM-Confidence:") : continue
	s=line.find(":")
	str=line[s+1:]
	value=float(str)
	count=count+1
	ss=value+ss
	# print(line)
	# print(count, ss, ss/count)
print('Average spam confidence:', ss/count)
#print("Done")
