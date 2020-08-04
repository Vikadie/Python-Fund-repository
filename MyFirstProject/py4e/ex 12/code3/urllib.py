import urllib.request, urllib.parse, urllib.error

#fhand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_42.html')
from bs4 import BeautifulSoup
import ssl

# ignore SSL certificate
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_42.html', context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

import re

print( sum( [ int(x) for x in re.findall('[0-9]+', soup) ] ) )
