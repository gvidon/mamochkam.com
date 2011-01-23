from mamochkam.apps.school.models import Direction
from django.conf.urls.defaults    import *
from django.conf                  import settings

urlpatterns = patterns('django.views.generic.simple',
	url(r'^raspisanie/?$', 'direct_to_template', {'template': 'school/raspisanie.html'}, name='school-raspisanie'),
)

urlpatterns += patterns('django.views.generic.list_detail',
	url(r'^$', 'object_list', {
		'allow_empty'  : True,
		'queryset'     : Direction.objects.all(),
		'template_name': 'school/index.html',
		'extra_context': {'MEDIA_URL': settings.MEDIA_URL},
	}, name='school'),
	
	url(r'^direction/(?P<slug>[_\-\d\w\s\.]+)/$', 'object_detail', {
		'slug_field'          : 'slug',
		'queryset'            : Direction.objects.all(),
		'template_name'       : 'school/direction.html',
		'template_object_name': 'direction',
	}, name='school-direction'),
)
