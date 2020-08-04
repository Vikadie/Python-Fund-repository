# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')

# http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times.
# The answer is the last name that you retrieve. (Fikret Montgomery Mhairade Butchi Anayah)

# http://py4e-data.dr-chuck.net/known_by_Aaliyah.html
# Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times.
count = input('Enter the count number: ')
c = int(count)
position = input('Enter the position number: ')
p = int(position)
cnt = 0
# Retrieve all of the anchor tags
while cnt < c:
    cnt = cnt + 1
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    pos = 0
    for tag in tags:
        if pos < p:
            pos = pos + 1
            t = (tag.get('href', None))
        else:
            print(t)
            url = t
            break
