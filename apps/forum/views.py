# -*- coding: utf-8 -*-
from datetime                       import datetime

from django.contrib.auth.decorators import login_required
from django.template.context        import RequestContext
from django.core.exceptions         import ValidationError
from django.views.generic           import list_detail
from django.shortcuts               import render_to_response
from django.conf                    import settings
from django.http                    import HttpResponse, Http404

from models import Thread, ThreadComment

#ВСЕ СООБЩЕНИЯ ВЕТКИ
def thread(request, id, page=1):
	try:
		thread = Thread.objects.get(id=id)
		
		return list_detail.object_list(request,
			queryset      = thread.comments.all(),
			paginate_by   = settings.ITEMS_PER_PAGE,
			page          = page,
			allow_empty   = True,
			template_name = 'forum/thread.html',
			extra_context = { 'thread': thread }
		)
		
	except Thread.DoesNotExist:
		raise Http404

#СОЗДАТЬ НОВУЮ ТЕМУ
@login_required
def new_thread(request):
	error = {}
	
	if request.POST:
		if not request.POST.get('title'):
			error['title'] = u'У обсуждения обязательно должна быть тема'
			
		if not request.POST.get('description'):
			error['description'] = u'Нужны подробности'
		
		if not error:
			thread = Thread.objects.create(
				user        = request.user,
				title       = request.POST['title'],
				description = request.POST['description']
			)
			
			thread.attach_tags(request.POST['tags'])
		
	return render_to_response('forum/new-thread.html', {
		'title'      : request.POST.get('title'),
		'description': request.POST.get('description'),
		'error'      : error,
		'thread_id'  : locals().has_key('thread') and thread.id or 0
	}, context_instance=RequestContext(request))
