# -*- coding: utf-8 -*-
from django.conf.urls.defaults   import *
from django.contrib              import admin

from mamochkam.apps.portal.views import advert_redirect, index
from mamochkam.apps.common.views import comment

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^comment/(?P<type>article|photo|forum|video)/(?P<id>[0-9]+)/?$', comment        , name='make-comment'),
	url(r'^advert-redirect/(?P<banner_id>[0-9]+)/?$'                     , advert_redirect, name='advert-redirect'),
	url(r'^/?$'                                                          , index          , name='index'),
	
	url(r'^bulletins/?', include('mamochkam.apps.bulletins.urls')),
	url(r'^pressroom/' , include('mamochkam.apps.pressroom.urls')),
	url(r'^photos/'    , include('mamochkam.apps.photos.urls')),
	url(r'^video/'     , include('mamochkam.apps.video.urls')),
	url(r'^forum/'     , include('mamochkam.apps.forum.urls')),
	url(r'^user/'      , include('mamochkam.apps.users.urls')),
	url(r'^search/'    , include('mamochkam.apps.search.urls')),
	url(r'^school/'    , include('mamochkam.apps.school.urls')),
	url(r'^magazine/'  , include('mamochkam.apps.magazine.urls')),
	url(r'^info/'      , include('mamochkam.apps.static.urls')),
	url(r'^shop/'      , include('mamochkam.apps.candy.urls')),
	url(r'^consults/'  , include('mamochkam.apps.consults.urls')),
	url(r'^nanny/'     , include('mamochkam.apps.nanny.urls')),
)

try:
	urlpatterns += patterns('',	url('^admin/(.*)', admin.site.root))
except AttributeError:
	urlpatterns += patterns('',	url('^admin/(.*)', admin.site.urls))


