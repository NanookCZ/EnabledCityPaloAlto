"""
This is only python file for admin of the app.
You can setup city, locations, lat, lng and category, that you want,
and run this script in python manage.py shell as
python load.py, where data will be loaded to your database
"""
import urllib2
import json

from django.db import models
from locations.models import Location

def find():
	url = 'https://api.foursquare.com/v2/venues/search?v=20131016&ll=37.4418800%2C%20%20-122.1430200&limit=100&intent=checkin&radius=1000&categoryId=4d4b7105d754a06374d81259&oauth_token=UPTDPXONO1BBJCM53FQ3HYFFBZ5MW5HG4NUQYYE0XCDNBX5I HTTP/1.1'
	obj = urllib2.urlopen(url)
	data = json.load(obj)
	locations = []
	for abc in data['response']['venues']:
		locations.append([abc['name'], str(abc['location']['lat']), str(abc['location']['lng']), abc['location']['city'], abc['categories'][0]['name']])
	return locations

def zapis():
	hovno = find()
	print hovno
	for h in hovno:
		location = Location()
		location.name = h[0]
		location.lat = h[1]
		location.lng = h[2]
		location.address = h[3]
		location.category = '4d4b7105d754a06374d81259'
		location.save()
	print "Created"
