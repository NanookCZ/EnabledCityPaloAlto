from django.conf import settings
from django.conf.urls import patterns, include, url
from locations.views import HomePageView, CultureView, FoodView, SportView, HospitalView, ParkingView, PublicView, TravelView, WCView
from locations.models import Location

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT }),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT }),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^category/cultures$', CultureView.as_view(), name='culture'),
    url(r'^category/foods$', FoodView.as_view(), name='food'),
    url(r'^category/sports$', SportView.as_view(), name='sport'),
    url(r'^category/hospitals$', HospitalView.as_view(), name='hospital'),
    url(r'^category/parking$', ParkingView.as_view(), name='parking'),
    url(r'^category/public$', PublicView.as_view(), name='public'),
    url(r'^category/travel$', TravelView.as_view(), name='travel'),
    url(r'^category/wc$', WCView.as_view(), name='wc'),
)