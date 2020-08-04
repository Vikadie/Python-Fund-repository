# Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.
# Use words.txt as the file name

while True :
	fname = input("Enter file name: ")
	try:
		fh = open(fname)
		break
	except:
		print("This file doesn't exist. Please try again!")
		continue
for line in fh:
	line = line.rstrip()
	ans = line.upper()
	print(ans)