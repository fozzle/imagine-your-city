from django.db import models

# Create your models here.
class MapPost(models.Model):
	"""Represents a user submission of a 
	photo/location"""

	# Metadata
	image = models.ImageField()
	date_submitted = models.DateTimeField(auto_add_now=true)
	title = models.CharField(max=200, blank=True)

	# Coordinate data
	latitude = models.FloatField()
	longitude = models.FloatField()
	
	

