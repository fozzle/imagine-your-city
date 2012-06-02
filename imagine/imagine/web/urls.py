from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('imagine.web.views',
    # Examples:
    url(r'^submit/$', 'submit', name='submit'),
    url(r'json/$', 'serve_data', name='serve_data'),
)