from django.conf import settings
from django.conf.urls.defaults import *
from models import Bulletin

urlpatterns = patterns('views',
	url(r'(?P<id>)[0-9+]/?'        , 'view'    , name='bulletin-view'   ),
	url(r'(?P<id>)[0-9+]/comment/?', 'comment' , name='bulletin-comment'),
)

urlpatterns += patterns('django.views.generic.list_detail',
	url(r'/?$', 'object_list', {
		'paginate_by'         : settings.ITEMS_PER_PAGE,
		'page'                : 1,
		'template_name'       : 'bulletins/index.html',
		'context_processors'  : ['RequestContext',],
		'template_object_name': 'bulletins',
		'queryset'            : Bulletin.objects.all()
	}, name='bulletins')
)
