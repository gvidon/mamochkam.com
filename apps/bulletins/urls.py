from django.conf.urls.defaults import *
from django.conf               import settings
from models                    import Bulletin

urlpatterns = patterns('mamochkam.apps.bulletins',
	url(r'add/?', 'add'),
)

# Bulletins list and details
urlpatterns += patterns('django.views.generic.list_detail',
	url(r'^(page/(?P<page>[0-9]+))?/?$', 'object_list', {
		'paginate_by': settings.ITEMS_PER_PAGE,
		'allow_empty': True,
		'queryset'   : Bulletin.objects.filter(publish=True),
	}, name='bt-list'),
	
	url(r'view/(?P<object_id>[0-9]+)/?$', 'object_detail', {
		'queryset' : Bulletin.objects.all(),
	}, name='bt-detail'),
)

# Month archive
urlpatterns += patterns('django.views.generic.date_based',
	url(r'archive/(?P<year>\d{4})/(?P<month>[a-z]{3})/$', 'archive_month', {
		'date_field'   : 'pub_date',
		'allow_empty'  : True,
		'queryset'     : Bulletin.objects.filter(publish=True),
		'template_name': 'bulletins/bulletins_list.html',
	}, name='bt-archive-month'),
)
