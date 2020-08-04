# ''' The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data,
# compute the sum of the numbers in the file.
# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_325696.xml (Sum ends with 9)'''
import urllib.request, urllib.parse, urllib.error

option = input('Choose option ("1" for Sample data,"2" for Actual data, other - quit): ')
if option == '1':
    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
    print('Retrieving: ', url)
elif option == '2':
    url = 'http://py4e-data.dr-chuck.net/comments_325696.xml'
    print('Retrieving: ', url)
else: quit()
xml_data = urllib.request.urlopen(url).read()
print('Retrieved', len(xml_data), 'characters')
#print(xml_data.decode())

import xml.etree.ElementTree as ET

tree = ET.fromstring(xml_data)
lst = tree.findall('comments/comment')
print('Comment count:', len(lst))
ss = 0
for item in lst:
    iter = ('Count:', item.find('count').text)
    ss = ss + int(iter[1])
print('Sum: ', ss)
