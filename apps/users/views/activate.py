# -*- coding: utf-8 -*-
import hashlib, random, datetime

from django.shortcuts            import render_to_response
from django.contrib.auth         import login
from django.contrib.auth.models  import User
from django.template.context     import RequestContext

from mamochkam.apps.users.models import Profile, Activation

ACCOUNT_MESSAGE = {
	'html': lambda username, password:
		'<html>'+
			'<head></head>'+
			'<body>'+
				'<p>Ваша учетная запись активирована. Теперь вы зарегистрированный пользователь'+
				'портала mamochkam.com.</p>'+
				
				'Логин: '+username.encode('utf8')+'<br/>'+
				'Пароль: '+password.encode('utf8')+'<br/>'+
			'</body>'+
		'</html>',
		
	'text': lambda username, password:
		'Ваша учетная запись активирована. Теперь вы зарегистрированный пользователь'+
		'портала mamochkam.com.\n\n'+
		'логин: '+username.encode('utf8')+' пароль: '+password.encode('utf8')
}

#GET ACTIVATION CODE BY URL
def by_url(request, code):
	if confirm(request, code):
		return render_to_response('user/activate/thanx.html', context_instance=RequestContext(request))
	
	else:
		return render_to_response('user/activate/wrong-code.html', context_instance=RequestContext(request))

#CONFIRM ACTIVATION AND LOGIN USER
def confirm(request, code):
	if not Activation.objects.filter(code=code, confirm_date=None).count():
		return 0
	
	for contact in Activation.objects.filter(code=code):
		try:
			# activate and set confirm_date to today date
			contact.user.is_active = 1
			(contact.response_date, contact.confirm_date) = [datetime.datetime.today()] * 2
			contact.save()
			
			# set user password if confirming activation request
			if contact.user.password == '!':
				password = generate_password(contact.user.id)
				
				contact.user.set_password(password)
				contact.user.save()
				
				contact.user.get_profile().send_email(
					'Учетная запись активирована',
					ACCOUNT_MESSAGE['text'](contact.user.username, password),
					ACCOUNT_MESSAGE['html'](contact.user.username, password)
				)
				
			
			contact.user.backend = 'django.contrib.auth.backends.ModelBackend'
			login(request, contact.user)
			
			contact.delete()
			
		except User.DoesNotExist:
			return 0
		
	return 1

#PASSWORD GENERATION ROUTINE
def generate_password(id):
	md5hash = hashlib.md5()
	md5hash.update(str(id+int(random.random()*50)))
	
	return md5hash.hexdigest()[:8]
