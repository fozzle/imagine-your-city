from django.core.management.base import BaseCommand, CommandError
from imagine.web.models import MapPost
import json, urllib2, datetime


class Command(BaseCommand):
    help = 'Grabs images tagged #IWISHTHISWAS'

    def handle(self, *args, **options):

        # Grab last map_pos
        try:
            last_map_post = MapPost.objects.all().order_by('date_submitted')[0]
        except:
            last_map_post = datetime.datetime(year=1980, month=1, day=1)


        # Grab images that are newer than the latest batch
        tag = "Iwishthiswas"

        # TODO: parmeterize tag?
        response = urllib2.urlopen("https://api.instagram.com/v1/tags/snow/media/"
                                   "recent?access_token=177352776.f59def8.a55d4cda6"
                                   "7eb4aa5af0a5663fd79a275")

        data = json.loads(response.read())

        for photo in data['data']:

            photo_date = datetime.datetime.fromtimestamp(float(photo['created_time']))
            if photo['location'] and photo['location'].has_key('latitude') and photo_date > last_map_post:
                MapPost.objects.create(date_submitted=photo_date, 
                                        caption=photo['caption']['text'],
                                        thumbnail=photo['images']['thumbnail']['url'],
                                        image=photo['images']['standard_resolution']['url'],
                                        latitude=photo['location']['latitude'],
                                        longitude=photo['location']['longitude'])
                print "Added one! \n"




