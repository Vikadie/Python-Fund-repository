
text = "X-DSPAM-Confidence:    0.8475";

#to print as float value the number at the end of this sentence using slice() and find()

x=text.find(":")
#print(x)
y=text[x+1:]
#z=y.strip()
w=float(z)
print(w)
