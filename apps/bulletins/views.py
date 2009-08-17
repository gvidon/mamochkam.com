# -*- coding: utf-8 -*-
import json, smtplib

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText      import MIMEText
from email.MIMEImage     import MIMEImage

from django.template.context import RequestContext
from django.shortcuts        import render_to_response
from django.http             import HttpResponse
from django.template         import RequestContext

from models import Bulletin
from forms  import BulletinForm

#AJAX: ADD NEW BULLETIN
def add(request):
	form = BulletinForm()
	
	if request.POST:
		form = BulletinForm(request.POST)
		
		if form.is_valid():
			Bulletin.objects.create(
				user_id     = 1,
				publish     = 0,
				title       = request.POST['title'],
				description = request.POST['description']
			)
			
			return render_to_response('bulletins/add.html', {}, context_instance = RequestContext(request))
		
	return render_to_response('bulletins/add.html', {
		'form': form
	}, context_instance = RequestContext(request))

#SEND BULLETIN REPLY TO OWNER'S EMAIL
def reply(request):
	if request.POST:
		try:
			bulletin = Bulletin.objects.get(id=request.POST['id'])
			
			if not(request.POST['contacts'] and request.POST['reply']):
				return HttpResponse(u'{ success: 0, error: "Необходимо заполнить все поля" }')
			
			msg = MIMEMultipart('alternative')
			
			msg['Subject'] = 'Кто-т ответил на ваше объявление'
			msg['From']    = 'no-reply@mamochkam.com'
			msg['To']      = bulletin.user.email

			msg.attach(MIMEText(
				'Ответ на <a href="http://mamochkam.com/bulletins/view/'+request.POST['id']+'">это объявление</a><br/>'+
				'<strong>Контактная информация</strong>: '+request.POST['contacts']+'<br/><br/>'+
				'<strong>Текст ответа</strong><br/>'+request.POST['reply']
			, _subtype='html', _charset='utf8'))
			
			msg.attach(MIMEText(
				'Ответ на http://mamochkam.com/bulletins/view/'+request.POST['id']+'\n'+
				'Контактная информация: '+request.POST['contacts']+'\n\n'+
				'Текст ответа\n'+request.POST['reply']
			, _subtype='plain', _charset='utf8'))

			s = smtplib.SMTP('localhost')
			s.sendmail(msg['From'], msg['To'], msg.as_string())
			s.quit()
			
			return HttpResponse('{ success: 1 }')
		
		except Bulletin.DoesNotExist, KeyError:
			return HttpResponse('{ success: 0 }')
