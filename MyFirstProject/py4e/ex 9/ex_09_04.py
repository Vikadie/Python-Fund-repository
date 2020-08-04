# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced,
# the program reads through the dictionary using a maximum loop to find the most prolific committer
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt" #runs automatically mbox-short.txt, with no need of typing anything
handle = open(name)

mails = dict()
for line in handle:
    line.rstrip()
    if not line.startswith('From ') :
        continue
    x = line.split()
    for mail in x:
        if '@' in mail: #to fill the dictionary mails only with word containing "@" (mail)
            mails[mail]=mails.get(mail,0)+1

bigcommitter = None
bignum = None
for mail,counts in mails.items(): #mail is the key, counts is the value
    if bignum is None or bignum < counts:
        bigcommitter = mail
        bignum = counts

print(bigcommitter, bignum)
