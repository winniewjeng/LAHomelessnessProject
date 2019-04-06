# importing the requests library
import requests
import os
import pprint

# api-endpoint
URL = "https://maps.googleapis.com/maps/api/geocode/json?address="
# location given here
location = "Apple Pasadena"
api = os.environ.get('GOOGLE_API_KEY')
URL = URL + location + "&key=" + api

# sending get request and saving the response as response object
r = requests.get(url=URL)

# extracting data in json format
data = r.json()

# print the data in terminal
pprint.pprint(data)

# extracting latitude, longitude and formatted address
# of the first matching location
latitude = data['results'][0]['geometry']['location']['lat']
longitude = data['results'][0]['geometry']['location']['lng']
formatted_address = data['results'][0]['formatted_address']

# printing the output
print("Latitude:%s\nLongitude:%s\nFormatted Address:%s" % (latitude, longitude, formatted_address))