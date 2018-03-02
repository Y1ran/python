# -*- coding: utf-8 -*-
"""
Created on Sat Mar 03 00:02:17 2018
Ver: python 2.7
@author: Administrator
"""


import json
import urllib
import sys

# Note that Google is increasingly requiring keys
# for this API
serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'
#'South Federal University'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.urlencode(
        {'address': address})

    print('Retrieving', url)
    uh = urllib.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))
    

    lat = js["results"]
    for item in lat:
        results = item.keys()
        values  = item.values()
        #print("")
    
    for i in range(len(results)):
        if results[i] == 'place_id':
            print("the place id is: " + values[i])
            location = js['results'][0]['formatted_address']
            print(location)
            
    break