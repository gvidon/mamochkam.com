from django.conf                 import settings
from django.conf.urls.defaults   import *

from mamochkam.apps.video.models import Video

# Video list and details
urlpatterns = patterns('django.views.generic.list_detail',
	url(r'^(page/(?P<page>[0-9]+))?/?$', 'object_list', {
		'paginate_by': settings.ITEMS_PER_PAGE,
		'allow_empty': True,
		'queryset'   : Video.objects.filter(publish=True),
	}, name='video-list'),
	
	url(r'view/(?P<object_id>[0-9]+)/?$', 'object_detail', {
		'queryset' : Video.objects.all(),
	}, name='video-detail'),
)

# Month archive
urlpatterns += patterns('django.views.generic.date_based',
	url(r'archive/(?P<year>\d{4})/(?P<month>[a-z]{3})/$', 'archive_month', {
		'date_field'   : 'pub_date',
		'allow_empty'  : True,
		'queryset'     : Video.objects.filter(publish=True),
		'template_name': 'video/video_list.html',
	}, name='video-archive'),
)
