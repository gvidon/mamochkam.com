from django.conf.urls.defaults    import *
from mamochkam.apps.school.models import Direction

urlpatterns = patterns('django.views.generic.simple',
	url(r'^raspisanie/?$', 'direct_to_template', {'template': 'school/raspisanie.html'}, name='school-raspisanie'),
)

urlpatterns += patterns('django.views.generic.list_detail',
	url(r'^$', 'object_list', {
		'allow_empty'  : True,
		'queryset'     : Direction.objects.all(),
		'template_name': 'school/index.html',
	}, name='school'),
	
	url(r'^direction/(?P<slug>[\-\d\w]+)/$', 'object_detail', {
		'slug_field'          : 'slug',
		'queryset'            : Direction.objects.all(),
		'template_name'       : 'school/direction.html',
		'template_object_name': 'direction',
	}, name='school-direction'),
)
