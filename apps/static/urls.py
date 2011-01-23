from django.conf.urls.defaults import *

urlpatterns = patterns('django.views.generic.simple',
	url(r'^$'                , 'direct_to_template', {'template': 'static/who-we-r.html'} , name='who-we-r'),
	url(r'^contacts/?$'      , 'direct_to_template', {'template': 'static/contacts.html'} , name='contacts'),
	url(r'^advert/?$'        , 'direct_to_template', {'template': 'static/advert.html'}   , name='advert'),
	
	url(r'^use/?$'           , 'direct_to_template', {'template': 'static/use-rules.html'}, name='use-rules'),
	url(r'^administration/?$', 'direct_to_template', {'template': 'static/admin.html'    }, name='admin'),
	
	url(r'^help/?$'          , 'direct_to_template', {'template': 'static/use-help.html'} , name='use-help'),
	url(r'^recover/?$'       , 'direct_to_template', {'template': 'static/recover.html' } , name='recover-help'),
	
	url(r'^training/?$'      , 'direct_to_template', {'template': 'static/training.html' } , name='training'),
)
