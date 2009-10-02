from django.conf                 import settings
from django.conf.urls.defaults   import *

from mamochkam.apps.forum.models import Thread

# Threads
urlpatterns = patterns('django.views.generic.list_detail',
	url(r'^(/page/(?P<page>[0-9]+)/?)?$', 'object_list', {
		'paginate_by': settings.ITEMS_PER_PAGE,
		'allow_empty': True,
		'queryset'   : Thread.objects.all(),
	}, name='threads'),
)

# Thread view
urlpatterns += patterns('mamochkam.apps.forum.views',
    url(r'thread/(?P<id>[0-9]+)/view(/page/(?P<page>[0-9]+))?/?$', 'thread', name='thread-view'),
)

# Month archive
urlpatterns += patterns('django.views.generic.date_based',
	url(r'archive/(?P<year>\d{4})/(?P<month>[a-z]{3})/$', 'archive_month', {
		'date_field'   : 'created_at',
		'allow_empty'  : True,
		'queryset'     : Thread.objects.all(),
		'template_name': 'forum/thread_list.html',
	}, name='forum-archive-month'),
)
urlpatterns += patterns('mamochkam.apps.forum.views',
	url(r'new-thread/?', 'new_thread', name='new-thread'),
)
