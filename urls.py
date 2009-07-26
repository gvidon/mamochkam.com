from django.conf.urls.defaults import *

urlpatterns = patterns('mamochkam.apps.portal.views',
	url(r'^/comment/(?P<type>article|photo|forum)/(?P<id>[0-9]+)/?$', 'comment', name='make-comment'),
	url(r'^/?$'                                                     , 'index'  , name='index'),
)

urlpatterns += patterns('',
	url(r'^bulletins/?', include('apps.bulletins.urls')),
	url(r'^pressroom/?', include('apps.pressroom.urls')),
	url(r'^photos/?'   , include('apps.photos.urls')),
)
