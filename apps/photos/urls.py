from django.conf import settings
from django.conf.urls.defaults import *

from apps.photos.models import Gallery

urlpatterns = patterns('mamochkam.apps.photos.views',
	url(r'upload/?$'                                    , 'upload' , name='upload-photo' ),
	url(r'(?P<slug>[a-zA-Z0-9_\-])/?(?P<page>[0-9]+?)?$', 'photos' , name='photos'       ),
)

urlpatterns += patterns('django.views.generic.list_detail',
	url(r'/?$', 'object_list', {
		'paginate_by'         : settings.ITEMS_PER_PAGE,
		'page'                : 1,
		'template_name'       : 'photos/index.html',
		'context_processors'  : ['RequestContext',],
		'template_object_name': 'galleries',
		'queryset'            : Gallery.objects.all()
	}, name='galleries')
)
