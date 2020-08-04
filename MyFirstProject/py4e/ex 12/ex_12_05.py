import urllib.request, urllib.parse, urllib.error

#fhand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_42.html')
from bs4 import BeautifulSoup
import ssl

# ignore SSL certificate
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_325694.html', context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

somme = 0

c = soup('span')
for s in c:
#    print('Span:', s) #check if soup('span') works
#    print('Comment:', s.contents[0]) # check if s.content[0] works
    num = int(s.contents[0]) #converts it to an integer
    somme = somme + num #store the sum of the integers up to now in variable somme
print(somme)

# Retrieve all of the anchor tags
#tags = soup('a')
#for tag in tags:
   # Look at the parts of a tag
 #  print 'TAG:',tag
 #  print 'URL:',tag.get('href', None)
 #  print 'Contents:',tag.contents[0]
 #  print 'Attrs:',tag.attrs
