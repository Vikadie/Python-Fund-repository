# prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data,
# compute the sum of the numbers in the file and enter the sum below
# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_325697.json (Sum ends with 27)
# print("PY4E")
import urllib.request, urllib.parse, urllib.error
import json

option = input('Make your choice (1-sample data; 2-actual data, other - quit()' )
if option == '1':
    url = 'http://py4e-data.dr-chuck.net/comments_42.json'
    print('Retrieving: ', url)
elif option == '2':
    url = 'http://py4e-data.dr-chuck.net/comments_325697.json'
    print('Retrieving: ', url)
else:
    if len(option)<1: quit()


js_data = urllib.request.urlopen(url).read().decode()
print('Retrieved' , len(js_data), 'characters.')

# print('JSON', js_data)
info = json.loads(js_data)
#print('INFO', info)
ss = 0 # intitalization of the Sum
lst = info['comments']
# print(lst) # check if info['comments'] can print and is really a list
print('Count:', len(lst))
#iteration in the list, comment is the index (sub of the lst)
for comment in lst:
    x = comment['count']
#    print('X ============', x) # check that on each iteration x moves to the next sub of the lst
    ss = ss + int(x)
print('Sum:', ss)
