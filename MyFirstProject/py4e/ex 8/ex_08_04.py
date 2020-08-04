# wprint('py4e')
# Open the file romeo.txt and read it line by line. For each line, split the line into a list of words
# using the split() method. The program should build a list of words. For each word on each line check to see
# if the word is already in the list and if not append it to the list. When the program completes,
# sort and print the resulting words in alphabetical order.
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line.rstrip()
    x = line.split() # split each line in list
    for wrd in x: # wrd is each word in the list x
        if wrd not in lst: # if the word wrd is not in the lst
            lst.append(wrd) # adds it to the list
lst.sort() #sort the list
print(lst) #print the list sorted
