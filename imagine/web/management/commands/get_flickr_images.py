from django.core.management.base import BaseCommand, CommandError
from imagine.web.models import MapPost
import json, urllib2, datetime
from imagine import settings


class Command(BaseCommand):
    help = 'Grabs images tagged #IWISHTHISWAS from flickr'

    def handle(self, *args, **options):

        # Grab last map_pos
        try:
            last_map_post = MapPost.objects.filter(source='1').order_by('-date_stored')[0].date_stored
        except:
        	last_map_post = datetime.datetime(year=1980, month=1, day=1)

        # Grab images that are newer than the latest batch
        tag = "Iwishthiswas"

        response = urllib2.urlopen("http://api.flickr.com/services/rest/?method=flickr.photos.search&"
        						   "api_key={key}&tags={tags}&min_upload_date={timestamp}&has_geo=1&format=json&nojsoncallback=1"
        						   .format(key=settings.FLICKR_KEY,
        						   			tags=tag,
        						   			timestamp=last_map_post.strftime("%s")))

        data = json.loads(response.read())

       	if data.has_key('photos'):

	        for photo in data['photos']['photo']:

				response = urllib2.urlopen("http://api.flickr.com/services/rest/?method=flickr.photos.getInfo&api_key={key}&photo_id={photo_id}"
											"&secret={secret}&format=json&nojsoncallback=1"
									   		.format(key=settings.FLICKR_KEY,
									   			photo_id=photo['id'],
									   			secret=photo['secret']))

				image_data = json.loads(response.read())

				image_data = image_data['photo']


				photo_url = ("http://farm{farm_id}.staticflickr.com"
							 "/{server_id}/{id}_{secret}.jpg"
							 .format(farm_id=photo['farm'],
							 		server_id=photo['server'],
							 		id=photo['id'],
							 		secret=photo['secret']))

				thumb_url = ("http://farm{farm_id}.staticflickr.com"
							 "/{server_id}/{id}_{secret}_t.jpg"
							 .format(farm_id=photo['farm'],
							 		server_id=photo['server'],
							 		id=photo['id'],
							 		secret=photo['secret']))

				photo_date = datetime.datetime.fromtimestamp(float(image_data['dates']['posted']))
				if image_data['location'] and image_data['location'].has_key('latitude') and photo_date > last_map_post:
				    MapPost.objects.create(date_submitted=photo_date, 
				                            caption=image_data['title']['_content'],
				                            thumbnail=thumb_url,
				                            image=photo_url,
				                            latitude=image_data['location']['latitude'],
				                            longitude=image_data['location']['longitude'],
				                            source='1'
					)
				    print "Added one! \n"
		else:
			print "No new photos found :( \n"