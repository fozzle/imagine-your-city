from django.utils import unittest
from django.test.client import Client
from imagine.web.models import MapPost

class TestSubmit(unittest.TestCase):
    def test_details(self):
        client = Client()
        with open('test.jpg') as fp:
        	response = client.post('/submit/', {'title': "Test!", 
        										'latitude':'33.7489', 
        										'longitude': '84.3881',
        										'image':fp})
        	self.assertEqual(response.status_code, 200)
        	self.assertEqual(MapPost.objects.get(pk=1).title, "Test!")
