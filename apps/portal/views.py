# -*- coding: utf-8 -*-
import json
import datetime

from django.shortcuts                import render_to_response
from django.shortcuts                import get_object_or_404
from django.template                 import RequestContext
from django.http                     import HttpResponseRedirect

from mamochkam.apps.pressroom.models import Article
from models                          import Banner

#РЕДИРЕКТ С БАННЕРА
def advert_redirect(request, banner_id):
	banner = get_object_or_404(Banner, pk=banner_id)
	
	banner.hits = int(banner.hits or 0) + 1
	banner.save()
	
	return HttpResponseRedirect(banner.url)

#PORTAL MAIN PAGE
def index(request):
	try:
		return render_to_response('portal/index.html', {
			'news': Article.objects.filter(is_news=True).order_by('-pub_date'),
		}, context_instance = RequestContext(request))
	
	except Article.DoesNotExist:
		return render_to_response('portal/index.html', {
			'news': [],
		}, context_instance = RequestContext(request))
