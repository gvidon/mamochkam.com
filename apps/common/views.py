# -*- coding: utf-8 -*-
import json
import datetime

from django.template  import RequestContext
from django.shortcuts import render_to_response

#from mamochkam.apps.forum.models     import Thread
from mamochkam.apps.pressroom.models import Article
from mamochkam.apps.photos.models    import Photo
from mamochkam.apps.tags.models      import Tag

comments_mapping = {
	'photo'  : Photo,
	'article': Article,
	#'forum'  : Thread,
}

#AJAX: COMMENTING INTERFACE
#**WARN** @login_required
def comment(request, type, id):
	if(request.POST):
		try:
			
			return HttpResponse(json.dumps({
				'success': 1,
				'pubdate': comment_mapping[type].objects.get(id=id).comments.create(
					user=request.user,
					text=request.POST['comment']
				).pub_date
			}))
			
		except KeyError, Photo.DoesNotExist:
			return HttpResponse(u'{ success: 0, message: "Ошибка в переданных параметрах" }')
	
	return HttpResponse(u'Объект не предназначен для просмотра браузером')
