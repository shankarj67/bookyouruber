'''
import googlemaps 
import re

# Requires API key 
gmaps = googlemaps.Client(key='AIzaSyAQB4eiCnuP8RXt0xPLYmsCDqrWX4iFKGc')  
# Requires cities name 
distance = gmaps.distance_matrix("12.927880, 77.627600",'13.035542, 77.597100')['rows'][0]['elements'][0]
distance_a = distance['duration']['text']
time  =re.search(r'[0-9]+', distance_a)
result = int(time[0])
print(f"time from a to b is {result}")
'''

import requests
source_lon = "12.927880"
source_lat = "77.627600"
url = f'https://rr1iky5f5f.execute-api.us-east-1.amazonaws.com/api/estimate/time?start_longitude={source_lon}&start_latitude={source_lat}'
print(url)
r = requests.get(url)
result = r.json()
time_second = int(result['times'][0]['estimate'])
time = time_second // 60
print(time)

