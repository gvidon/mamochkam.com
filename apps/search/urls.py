from django.conf.urls.defaults import *

urlpatterns = patterns('mamochkam.apps.search.views',
	url(r'^by-tag/(?P<tag>[ \w\d\-\.,_]+)/(?P<object_type>(article|forum|photo|video)+)/?$', 'by_tag', name='search-by-tag'),
	#url(r'^(?P<text>[\w\d\-\.,_]+)/(?P<object_type>(all|article|forum|photo|video)+)/?$'      , 'all'   , name='search'),
)
