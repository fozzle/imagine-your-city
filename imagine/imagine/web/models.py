from django.db import models

# Create your models here.
class MapPost(models.Model):
	"""Represents a user submission of a 
	photo/location"""

	# Metadata
	image = models.ImageField(upload_to='uploads/')
	date_submitted = models.DateTimeField(auto_now=True)
	title = models.CharField(max_length=200, blank=True)

	# Coordinate data
	latitude = models.FloatField()
	longitude = models.FloatField()
	
	

