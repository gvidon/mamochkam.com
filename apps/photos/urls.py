from django.conf import settings
from django.conf.urls.defaults import *

from apps.photos.models import Gallery, Photo

urlpatterns = patterns('mamochkam.apps.photos.views',
	url(r'upload/?$', 'upload' , name='ph-upload'),
)

# Photo list and details
urlpatterns += patterns('django.views.generic.list_detail',
	url(r'^(page/(?P<page>[0-9]+))?/?$', 'object_list', {
		'paginate_by': settings.ITEMS_PER_PAGE,
		'allow_empty': True,
		'queryset'   : Photo.objects.filter(publish=True),
	}, name='ph-photo-list'),
	
	url(r'view/(?P<object_id>[0-9]+)/?$', 'object_detail', {
		'queryset' : Photo.objects.all(),
	}, name='ph-photo-detail'),
)

# Photo galleries
urlpatterns += patterns('mamochkam.apps.photos.views',
    url(r'^gallery/(?P<slug>[\-\d\w]+)(/page/(?P<page>[0-9]+)/?)?$', 'view_gallery', name='ph-gallery-page')
)

# Month archive
urlpatterns += patterns('django.views.generic.date_based',
	url(r'archive/(?P<year>\d{4})/(?P<month>[a-z]{3})/$', 'archive_month', {
		'date_field'   : 'pub_date',
		'allow_empty'  : True,
		'queryset'     : Photo.objects.filter(publish=True),
		'template_name': 'photos/photo_list.html',
	}, name='ph-archive-month'),
)
