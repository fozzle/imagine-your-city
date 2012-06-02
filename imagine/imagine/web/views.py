from imagine.web.forms import SubmitForm
from imagine.web.models import MapPost
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse, HttpResponseBadRequest


def home(request):
	# Retreive all listings (for now, in the future we will narrow it down)
	posts = MapPost.objects.all()
	return render_to_response("index.html", {}, RequestContext(request))

def submit(request):
	# Take post request from phone, all data needs to be processed
	# and placed into a MapPost model
	if request.method == 'POST':
		post = SubmitForm(request.POST, request.FILES)
		if post.is_valid():
			post = post.save()
			return HttpResponse("<html><body>Success!</body></html>")

	return HttpResponseBadRequest("Now you fucked up.")