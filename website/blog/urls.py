from django.conf.urls import *

from blog.views import archive
from blog.views import pages

urlpatterns = patterns('', 
			url(r'^$',     archive, name='blog'),
			url(r'page1/(?P<name>[a-z0-9\s]+)/$', pages)
			
			#url(r'page(?P<num>[0-9]+)/$', pages)
			)
