var map

function initialize() {
  var myOptions = {
    center: new google.maps.LatLng(-34.397, 150.644),
    zoom: 8,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  };
  map = new google.maps.Map(document.getElementById("map_canvas"),
      myOptions);

  var image = new google.maps.MarkerImage('static/img/icon.png',
              // This marker is 20 pixels wide by 32 pixels tall.
              new google.maps.Size(25, 16),
              // The origin for this image is 0,0.
              new google.maps.Point(0,0),
              // The anchor for this image is the base of the flagpole at 0,32.
              new google.maps.Point(12, 16));
  // Add markers
  {% for photo in photos_list %}
  var marker{{photo.id}} = new google.maps.Marker({
    position: new google.maps.LatLng({{ photo.latitude }}, {{ photo.longitude }}), 
    map: map,
    icon: image,
    title: '{{ photo.caption }}'
  });   

  var contentString{{ photo.id }} = '<a href="{{ photo.image }}"><img src="{{photo.thumbnail}}"></a><p>{{ photo.caption }}</p>';
  
  var infowindow{{ photo.id }} = new google.maps.InfoWindow({
      content: contentString{{ photo.id }},
      maxWidth: 150
  });

  // Listen for click
  google.maps.event.addListener(marker{{ photo.id }}, 'click',function() {
      infowindow{{ photo.id }}.open(map,marker{{ photo.id }});
  });
}

// Try HTML5 geolocation
if(navigator.geolocation) {
  navigator.geolocation.getCurrentPosition(function(position) {
    var pos = new google.maps.LatLng(position.coords.latitude,
                                     position.coords.longitude);

    map.setCenter(pos);
  }, function() {
    handleNoGeolocation(true);
  });
}