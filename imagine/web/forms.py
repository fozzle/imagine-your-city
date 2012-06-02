from django import forms
from imagine.web.models import MapPost

# Do we need forms?
# Placeholder for future features.

# Yes we do.
class SubmitForm(forms.ModelForm):
	
	class Meta:
		model = MapPost
		exclude = {'date_submitted'}