# importing the requests library
import requests
import os
import pprint
import time
import matplotlib.pyplot as plt
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np

addresses = []
names = []
cities = []

file = r'Mental Health Service Providers January 2016.xlsx'
df = pd.read_excel(file)

rows_len = len(df)
i = 0
while i != rows_len:
    addresses.append(df['Address'][i] + ', ' + df['City'][i])
    cities.append(df['City'][i])
    names.append(df['Provider Name'][i])
    # print(addresses[i])  # check
    # print(df['Address'][i] + ', ' + df['City'][i] +'\n')  # double-check
    i = i + 1

# dictionary of address and lat and long
geoLocations = {}
lat = []
lon = []
j = 0
# api call to get the coordinates
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
    lat.append(latitude)
    lon.append(longitude)
    # printing the output
    print("Formatted Address:%s\nLatitude:%s\nLongitude:%s\nName:%s" % (formatted_address, latitude, longitude, names[j]))
    # storing things inside the geoLocations dictionary
    j = j + 1

    # make the request with exponential-backoff:
    time.sleep(0.05)
    # https://stackoverflow.com/questions/28650264/script-for-creating-dictionary-from-coordinates

print('\nparsing completed')

df = pd.DataFrame({'lat': lat,
                   'long': lon,
                   'city': cities,
                   'name:': names})
writer = ExcelWriter('Lat_Long_Mental_Health_Service_Provider_1.xlsx')
df.to_excel(writer, 'Sheet1', index=False)
writer.save()
