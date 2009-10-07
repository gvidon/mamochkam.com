# -*- coding: utf-8 -*-
try:
	from json import dumps
except ImportError:
	from json import write as dumps
	
import datetime

from django.contrib.auth.decorators  import login_required
from django.core.exceptions          import ValidationError
from django.template.loader          import render_to_string
from django.template                 import RequestContext
from django.shortcuts                import render_to_response
from django.http                     import HttpResponse, Http404

from mamochkam.apps.pressroom.models import Article
from mamochkam.apps.search.models    import Tag
from mamochkam.apps.photos.models    import Photo
from mamochkam.apps.forum.models     import Thread
from mamochkam.apps.video.models     import Video

entities = {
	'photo'  : Photo,
	'article': Article,
	'forum'  : Thread,
	'video'  : Video,
}

#AJAX: COMMENTING INTERFACE
@login_required
def comment(request, type, id):
	if(request.POST):
		try:
			
			if not request.POST['comment']:
				raise ValidationError
			
			pub_date = entities[type].objects.get(id=id).comments.create(
				user=request.user,
				text=request.POST['comment']
			).pub_date
			
			return HttpResponse(dumps({
				'success': 1,
				'date'   : str(pub_date),
				'fresh'  : render_to_string('common/_comments-core.html', {
					'comments': entities[type].objects.get(id=id).comments.filter(
						pub_date__gt=request.POST['since']
					).order_by('pub_date')
				}, context_instance=RequestContext(request)).decode('utf8')
			}))
			
		except (KeyError, Article.DoesNotExist, Photo.DoesNotExist):
			return HttpResponse(u'{ success: 0, error: "Ошибка в переданных параметрах" }')
			
		except ValidationError:
			return HttpResponse(u'{ success: 0, error: "Нужен комментарий" }')
	
	return HttpResponse(u'Объект не предназначен для просмотра браузером')
