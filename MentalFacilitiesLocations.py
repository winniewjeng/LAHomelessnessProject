# importing the requests library
import requests
import os
import csv
import pprint
import time

addresses = []
f = open('Mental_Health_Service_Providers_2016.csv')
csv_f = csv.reader(f)

for row in csv_f:
    address = row[2] + ', ' + row[3]
    addresses.append(address)
    # print(row[2]+' '+row[3])


# dictionary of address and lat and long
geoLocations = {}
lat = []
lon = []

del addresses[0]


for location in addresses:
    # print(location + '\n')
    # api-endpoint
    URL = "https://maps.googleapis.com/maps/api/geocode/json?address="
    # api key
    api = os.environ.get('GOOGLE_API_KEY')
    # # building the url
    URL = URL + location + "&key=" + api
    # sending get request and saving the response as response object
    r = requests.get(url=URL)
    # extracting data in json format
    data = r.json()
    # pprint.pprint(data)  # print the data in terminal
    # extracting latitude, longitude and formatted address of the first matching location
    formatted_address = data['results'][0]['formatted_address']
    latitude = data['results'][0]['geometry']['location']['lat']
    longitude = data['results'][0]['geometry']['location']['lng']
    # printing the output
    print("Latitude:%s\nLongitude:%s\nFormatted Address:%s" % (latitude, longitude, formatted_address))
    # storing things inside the geoLocations dictionary

    # make the request with exponential-backoff:
    time.sleep(0.1)

# https://stackoverflow.com/questions/28650264/script-for-creating-dictionary-from-coordinates