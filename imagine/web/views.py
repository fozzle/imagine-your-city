from imagine.web.forms import SubmitForm
from imagine.web.models import MapPost
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse, HttpResponseBadRequest
import json


def home(request):
	# Retreive all listings (for now, in the future we will narrow it down)
	photos_list = MapPost.objects.all()
	return render_to_response("index.html", {'photos_list': photos_list}, RequestContext(request))

def serve_data(request):

	# Retreive all listings, return json string.

	photos_list = MapPost.objects.all()

	photos_json = []
	for photo in photos_list:
		photos_json.append({'caption': photo.caption,
							'thumbnail': photo.thumbnail,
							'image': photo.image,
							'date_submitted': str(photo.date_submitted),
							'latitude': photo.latitude,
							'longitude': photo.longitude})

	return HttpResponse(json.dumps(photos_json), mimetype="application/json")

def submit(request):
	# Take post request from phone, all data needs to be processed
	# and placed into a MapPost model
	if request.method == 'POST':
		post = SubmitForm(request.POST, request.FILES)
		if post.is_valid():
			post = post.save()
			return HttpResponse("<html><body>Success!</body></html>")

	return HttpResponseBadRequest("Now you fucked up.")