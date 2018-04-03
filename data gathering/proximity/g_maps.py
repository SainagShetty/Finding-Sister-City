import requests
import pandas as pd
import math

df = pd.read_csv('proximity.csv')
# address = "Ashford town, Alabama"
api_key = "AIzaSyABD0S22o7uZJeHlqXTl-efJ5aa8RBg4V0"
# api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
# api_response_dict = api_response.json()

# if api_response_dict['status'] == 'OK':
#     latitude = api_response_dict['results'][0]['geometry']['location']['lat']
#     longitude = api_response_dict['results'][0]['geometry']['location']['lng']
#     print 'Latitude:', latitude
#     print 'Longitude:', longitude

lat = []
longi = []
j = 0
n = 0
for index, row in df.iterrows():
	if math.isnan(row.lat) or math.isnan(row.lng):
		address = row['Geography'] + ", " + row['stateFullName']
		api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
		api_response_dict = api_response.json()
		if api_response_dict['status'] == 'OK':
			lat.append(api_response_dict['results'][0]['geometry']['location']['lat'])
			longi.append(api_response_dict['results'][0]['geometry']['location']['lng'])
			row['lat'] = api_response_dict['results'][0]['geometry']['location']['lat']
			row['lng'] = api_response_dict['results'][0]['geometry']['location']['lng']
			n += 1
			print n, address
		else:
			print "Error!"
df.to_csv('pro.csv')