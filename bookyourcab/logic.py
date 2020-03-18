import googlemaps 
import re
import requests
from conf.settings import Google_DATA_API_KEY as api_key





def calculate_google_map_timing(source, destination): 
    gmaps = googlemaps.Client(key=api_key)  
    distance = gmaps.distance_matrix(
        source, destination
        )['rows'][0]['elements'][0]
    distance_a = distance['duration']['text']
    time  =re.search(r'[0-9]+', distance_a)
    result = int(time[0])
    return result


def calculate_uber_timing(source):
    source = source.split(",")
    source_lon = source[0]
    source_lat = source[1]
    url = f'https://rr1iky5f5f.execute-api.us-east-1.amazonaws.com/api/estimate/time?start_longitude={source_lon}&start_latitude={source_lat}'
    r = requests.get(url)
    result = r.json()
    time_second = int(result['times'][0]['estimate'])
    time = time_second // 60
    
    return time

def send_mail(given_time):
    pass