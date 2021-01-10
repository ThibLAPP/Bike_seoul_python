from django.db import models

class Bike(models.Model):
	hour			= models.IntegerField()
	temp			= models.FloatField()
	humidity		= models.IntegerField()
	wind_speed		= models.FloatField()
	visibility		= models.IntegerField()
	solar_rad		= models.FloatField()
	rainfall		= models.FloatField()
	snowfall		= models.FloatField()
	season			= models.CharField(max_length=10, choices = [('Winter', 'Winter'), ('Autumn', "Autumn"), ('Summer', 'Summer'), ('Spring', 'Spring')])
	holiday			= models.CharField(max_length=10, choices = [('Holiday', 'Holiday'), ('Holiday', 'No Holiday')])

