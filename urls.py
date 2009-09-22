from django.conf.urls.defaults   import *
from django.contrib              import admin

from mamochkam.apps.portal.views import index
from mamochkam.apps.common.views import comment

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^comment/(?P<type>article|photo|forum)/(?P<id>[0-9]+)/?$', comment, name='make-comment'),
	url(r'^/?$'                                                    , index  , name='index'),
	
	url(r'^bulletins/?'                                            , include('mamochkam.apps.bulletins.urls')),
	url(r'^pressroom/?'                                            , include('mamochkam.apps.pressroom.urls')),
	url(r'^photos/'                                                , include('mamochkam.apps.photos.urls')),
	url(r'^forum/'                                                 , include('mamochkam.apps.forum.urls')),
	url(r'^user/'                                                  , include('mamochkam.apps.users.urls')),
)

urlpatterns += patterns('',
	url('^admin/(.*)', admin.site.root),
)

