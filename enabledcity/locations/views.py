from django.views import generic
from django.core.urlresolvers import reverse_lazy
from locations.models import Location

class HomePageView(generic.ListView):
	template_name = 'home.html'
	model = Location
	context_object_name = 'location'


class CultureView(generic.ListView):
	template_name = 'places/culture.html'
	model = Location
	context_object_name = 'culture_list'
	queryset = Location.places.filter(category = '4d4b7104d754a06370d81259')


class FoodView(generic.ListView):
	template_name = 'places/food.html'
	model = Location
	context_object_name = 'food_list'
	queryset = Location.places.filter(category = '4d4b7105d754a06374d81259')

class HospitalView(generic.ListView):
	template_name = 'places/hospital.html'
	model = Location
	context_object_name = 'hospital_list'
	queryset = Location.places.filter(category = '4bf58dd8d48988d104941735')

class SportView(generic.ListView):
	template_name = 'places/sport.html'
	model = Location
	context_object_name = 'sport_list'
	queryset = Location.places.filter(category = '4d4b7105d754a06377d81259')

class ParkingView(generic.ListView):
	template_name = 'places/parking.html'
	model = Location
	context_object_name = 'parking_list'
	queryset = Location.places.filter(category = '4c38df4de52ce0d596b336e1')

class PublicView(generic.ListView):
	template_name = 'places/public.html'
	model = Location
	context_object_name = 'public_list'
	queryset = Location.places.filter(category = '4d4b7105d754a06375d81259')

class TravelView(generic.ListView):
	template_name = 'places/travel.html'
	model = Location
	context_object_name = 'travel_list'
	queryset = Location.places.filter(category = '4d4b7105d754a06379d81259')

class WCView(generic.ListView):
	template_name = 'places/wc.html'
	model = Location
	context_object_name = 'wc_list'
	queryset = Location.places.filter(category = '4bf58dd8d48988d130941735')