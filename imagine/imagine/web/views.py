from imagine.web.models import MapPost
from django.shortcuts import render_to_response
from django.template.context import RequestContext


def home(request):
	return render_to_response("index.html", {}, RequestContext(request))

def submit(request):
	pass
	# Take post request from phone, all data needs to be processed
	# and placed into a MapPost model
	if request.method == 'POST':
