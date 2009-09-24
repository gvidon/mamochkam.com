from django.conf.urls.defaults import *

urlpatterns = patterns('mamochkam.apps.users.views',
	url(r'^register/?'                        , 'register.form'),
	url(r'^activate/(?P<code>[0-9a-zA-Z]+)/?$', 'activate.by_url'),
	
	url(r'^profile/?$'                        , 'profile.form'),
)

urlpatterns += patterns('',
	url(r'^login/?$' , 'django.contrib.auth.views.login', { 'template_name': 'user/login.html' }),
	url(r'^logout/?$', 'django.contrib.auth.views.logout_then_login'),
)

urlpatterns += patterns('mamochkam.apps.users.views',
	url(r'^(?P<username>[\w\d\-_\.]+)/?', 'public.profile', name='public-profile'),
)
