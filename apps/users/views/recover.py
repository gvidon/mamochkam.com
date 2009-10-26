# -*- coding: utf-8 -*-
import hashlib
import random
import re

from datetime                    import datetime

from django.contrib.auth.models  import User
from django.template.loader      import render_to_string
from django.shortcuts            import render_to_response
from django.http                 import Http404
from django.template             import RequestContext

from mamochkam.apps.users.models import Profile
from mamochkam.apps.users.models import Activation

#ПОДТВЕРЖДЕНИЕ ВОССТАНОВЛЕНИЯ ПАРОЛЯ
def confirm(request, code):
	try:
		plain_password = hashlib.md5(str(random.random())).hexdigest()[:8]
		
		activation = Activation.objects.get(
			value         = code,
			type          = 'password',
			confirm_date  = None
		)
		
		activation.user.set_password(plain_password)
		activation.user.save()
		
		email_html = render_to_string('mail/recover-confirmed.html', {
			'login'   : activation.user.username,
			'password': plain_password,
		}).encode('utf8')
		
		activation.user.get_profile().send_email(
			'Новый пароль учетной записи',
			
			# убрать тэги в текстовой части письма
			re.compile(r'<.*?>').sub('', email_html),
			email_html
		)
		
		activation.response_date = datetime.today()
		activation.confirm_date = datetime.today()
		activation.save()
		
	except Activation.DoesNotExist:
		raise Http404
		
	return render_to_response('user/recover/thanx.html', {
		'email': activation.user.email
	}, context_instance=RequestContext(request))

#EMAIL FORM FOR PASSWORD CONFIRMATION
def form(request):
	error = ''
	
	if request.POST:
		try:
			user = User.objects.get(email=request.POST['email'])
			code = hashlib.md5(str(random.random())).hexdigest()
			
			Activation.objects.create(
				user  = user,
				type  = 'password',
				value = code
			)
			
			email_html = render_to_string('mail/recover.html', { 'code': code }).encode('utf8')
			
			user.get_profile().send_email(
				'Восстановление пароля учетной записи',
				
				# убрать тэги в текстовой части письма
				re.compile(r'<.*?>').sub('', email_html),
				email_html
			)
			
		except KeyError:
			error = u'А где же e-mail?'
		
		except User.DoesNotExist:
			error = u'Учетной записи с таким e-mail нет в нашей базе.'
	
	return render_to_response('user/recover/form.html', {'error': error}, context_instance=RequestContext(request))
