# -*- coding: utf-8 -*-
from django.conf                    import settings
from django.conf.urls.defaults      import *

from mamochkam.apps.consults.models import Question

#ВОПРОСЫ
urlpatterns = patterns('django.views.generic.list_detail',
	url(r'^(/page/(?P<page>[0-9]+)/?)?$', 'object_list', {
		'paginate_by': settings.ITEMS_PER_PAGE,
		'allow_empty': True,
		'queryset'   : Question.objects.all().order_by('master__profiles__consults_in'),
	}, name='questions'),
)

#ОТВЕТЫ
urlpatterns += patterns('mamochkam.apps.consults.views',
	url(r'question/(?P<id>[0-9]+)/answer/?$', 'answer'      , name='answer'),
	url(r'question/(?P<id>[0-9]+)/?$'       , 'question'    , name='question'),
	url(r'question/add/?'                   , 'new_question', name='new-question'),
)

