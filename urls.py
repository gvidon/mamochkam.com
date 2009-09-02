from django.conf.urls.defaults import *
from django.contrib            import admin

admin.autodiscover()

urlpatterns = patterns('mamochkam.apps.portal.views',
	url(r'^/comment/(?P<type>article|photo|forum)/(?P<id>[0-9]+)/?$', 'comment', name='make-comment'),
	url(r'^/?$'                                                     , 'index'  , name='index'),
)

urlpatterns += patterns('',
	url(r'^bulletins/?', include('mamochkam.apps.bulletins.urls')),
	url(r'^pressroom/?', include('mamochkam.apps.pressroom.urls')),
	url(r'^photos/?'   , include('mamochkam.apps.photos.urls')),
	url(r'^forum/'     , include('mamochkam.apps.forum.urls')),
)

urlpatterns += patterns('',
	url('^admin/(.*)', admin.site.root),
)

