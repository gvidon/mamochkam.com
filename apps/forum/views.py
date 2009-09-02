# -*- coding: utf-8 -*-
from datetime import datetime

from django.conf             import settings
from django.template.context import RequestContext
from django.views.generic    import list_detail
from django.shortcuts        import render_to_response
from django.http             import HttpResponse, Http404

from models import Thread, ThreadComment

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
