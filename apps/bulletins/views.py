# -*- coding: utf-8 -*-
import json

from django.template.context import RequestContext
from django.shortcuts        import render_to_response
from django.http             import HttpResponse

from models import Bulletin
from forms  import BulletinForm

#AJAX: ADD NEW BULLETIN
def add(request):
	return HttpResponse(json.dumps({
		'success': 1,
		'pubdate': Bulletin.objects.create(
			user        = request.user,
			
			phone       = request.POST['phone'],
			email       = request.POST['email'],
			icq         = request.POST['icq'],
			
			title       = request.POST['title'],
			description = request.POST['description']
		).pub_date
	}))

#VIEW BULLETIN INFO
def view(request, id):
	try:
		return render_to_response(
			'bulletins/view.html',
			{ 'bulletins': Bulletin.objects.get(id=id) }
			context_instance = RequestContext
		)
	
	except Bulletin.DoesNotExist:
		return render_to_response('bulletins/does-not-exist.html', context_instance=RequestContext)
