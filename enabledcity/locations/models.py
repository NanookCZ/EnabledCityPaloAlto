from django.db import models

""""
dopisat acesible model manager
"""

class LocationManager(models.Manager):
	def accessible(self):
		return super(LocationManager, self).filter(accessible = True)

class Location(models.Model):
	DISABILITY_CHOICES = (
        ('accessible', 'acessible'),
        ('not accessible', 'not accessible')
    )
	name = models.CharField(max_length = 255)
	address = models.CharField(max_length = 255)
	lat = models.CharField(max_length = 125)
	lng = models.CharField(max_length = 125)
	#cover = models.ImageField(blank = True, null = True)
	accessible = models.CharField(max_length = 50, choices =DISABILITY_CHOICES, default = 'accessible')
	category = models.CharField(max_length = 125)
	places = LocationManager()
	
	

	def __unicode__(self):
		return self.name