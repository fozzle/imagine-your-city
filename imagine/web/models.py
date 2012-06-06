from django.db import models

class MapPost(models.Model):
	"""Represents a user submission of a 
	photo/location"""

	# Metadata
	image = models.CharField(max_length=400)
	thumbnail = models.CharField(max_length=400)

	# date_submitted represents the time the picture was taken
	date_submitted = models.DateTimeField(blank=True)

	# date stored is used for caching calculations, when the
	# data was stored in our db
	date_stored = models.DateTimeField(auto_now_add=True)

	caption = models.CharField(max_length=200, blank=True)

	# Coordinate data
	latitude = models.FloatField()
	longitude = models.FloatField()

	# Source of image
	# TODO: Howcome the friggin wipe DB isn't working!
	source = models.CharField(max_length=1, choices=[('0', 'instagram'),
													  ('1', 'flickr')])

