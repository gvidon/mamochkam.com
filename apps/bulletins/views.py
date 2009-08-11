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

#SEND BULLETIN REPLY TO OWNER'S EMAIL
def reply(request):
	if request.POST:
		try:
			bulletin = Bulletin.objects.get(id=request.POST['id'])
			
			try:
				server = smtplib.SMTP('localhost')
				server.sendmail(
					'From: no-reply@mamochkam.com',
					'To: '+bulletin.user.email,
					'Subject: На ваше объявление ответили\r\n'+request.POST['reply']
				)
				server.quit()
			
			except KeyError:
				return HttpResponse(u'{ success: 0, error: "Необходимо заполнить все поля" }')
			
			return HttpResponse('{ success: 1 }')
			
		except Bulletin.DoesNotExist, KeyError:
			return HttpResponse('{ success: 0 }')
