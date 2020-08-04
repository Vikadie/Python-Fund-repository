# The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data,
# and retrieve the first place_id from the JSON.
# A place ID is a textual identifier that uniquely identifies a place as within Google Maps.

# To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:
# http://py4e-data.dr-chuck.net/json?
# This API uses the same parameter (address) as the Google API. This API also has no rate limit so you can test as often as you like.
# If you visit the URL with no parameters, you get "No address..." response.
# To call the API, you need to provide the address that you are requesting as the address= parameter that is properly URL encoded
# using the urllib.parse.urlencode() function

# test : location of "South Federal University" which will have a place_id of "ChIJNeHD4p-540AR2Q0_ZjwmKJ8"

# Please run your program to find the place_id for this location:

# University of Oxford

# Make sure to enter the name and case exactly as above and enter the place_id and your Python code below.
# Hint: The first seven characters of the place_id are "ChIJW0i ..."
# Make sure to retreive the data from the URL specified above and not the normal Google API.

# print('py4e') # 1st thing to do: check line for python code

import urllib.request, urllib.parse, urllib.error
import json

# ======================================================
# mandatory api_Key part : if not used you get "Missing/incorrect key= parameter (it is an easy number to guess)..."
api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    service_url = 'http://py4e-data.dr-chuck.net/json?'
else :
    service_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
# mandatory api_Key part : if not used you get "Missing/incorrect key= parameter (it is an easy number to guess)..."
# ======================================================

#loop for entering the address
while True:
    location = input('Enter location: ')
    if len(location) < 1 : break

    # concatenating correctly the parameters - by using a dict()
    param = dict()
    param['address'] = location
    # again mandatory api_key part to add to my param dictionary the key=42 string =================================================
    if api_key is not False: param['key'] = api_key
    # again mandatory api_key part to add to my param dictionary the key=42 string =================================================
    print('Parameter:', param)
    print('Encoded parameter:', urllib.parse.urlencode(param))
    # concatenate the service url + address= parameter + location
    surl = service_url + urllib.parse.urlencode(param)
    # Print the url (with location included)
    print('Retrieving ', surl)
    # receiving the JSON and decoding it
    surl_resp = urllib.request.urlopen(surl).read().decode()
    # print the number of characters from received and decoded (readable) JSON
    print('Retrieved', len(surl_resp), 'characters')

    try:
        js = json.loads(surl_resp)
    except:
        js = None

    if not js or 'status' not or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print('===============================', surl_resp)
        continue

    print(json.dumps(js, indent=4))
    print('Answer for place_id:', js['results'][0]['place_id'])
