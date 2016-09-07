#!/usr/bin/env python
import urllib.request

from contextlib import closing
import urllib.request
import json
import sys
Url_Input = "www.lifestylerhythmsfitness.com.au" #this is the website you want to search
url = 'http://freegeoip.net/json/' + Url_Input
with closing(urllib.request.urlopen(url)) as response:
    for line in response:
        # print(line.decode('utf-8'))
        location = json.loads(line.decode('utf-8'))
        location_ip = location['ip']
        location_city = location['city']
        location_state = location['region_name']
        location_country = location['country_name']
        location_zip = location['zip_code']
        print("country : " + location_country)
        print("city : " + location_city)
        print("state : " + location_state)
        print("zip code : " + location_zip)
        print("ip : "+location_ip)
        print(location)
