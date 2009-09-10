# -*- coding: utf-8 -*-
import hashlib, random, httplib, urllib

from django.contrib.auth.models  import User
from django.template.context     import RequestContext
from django.shortcuts            import render_to_response

from mamochkam.apps.users.forms  import ProfileForm
from mamochkam.apps.users.models import Profile, Activation

ACTIVATION_MESSAGE = {
	'html': lambda code: unicode('''\
		<html>
			<head></head>
			<body>
				<a href="http://mamochkam.com/user/activate/'''+code+'''">http://mamochkam.com/user/activate/'''+code+'''</a>
			</body>
		</html>'''),
	
	'text': lambda code: 'http://mamochkam.com/user/activate/'+code
}

#REGISTER USER'S INFO AND SEND CONFIRMATION LINK
def form(request):
	form = ProfileForm(auto_id='%s')
	
	if request.POST:
		form = ProfileForm(auto_id='%s', data=request.POST)
		
		if(form.is_valid()):
			# create DISABLED user
			user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], '')
			
			user.first_name = form.cleaned_data.get('first_name')
			user.last_name  = form.cleaned_data.get('last_name')
			
			user.is_active  = 0
			
			user.save()
			
			# populate user's profile
			Profile.objects.create(
				user       = user,
				auth_type  = 'local',
				sur_name   = form.cleaned_data.get('sur_name')
			)
			
			# prepare activation code
			md5hash = hashlib.md5()
			md5hash.update(str(user.id+int(random.random()*50)))
			
			Activation.objects.create(
				user  = user,
				type  = 'email',
				value = form.cleaned_data['email'],
				code  = md5hash.hexdigest()
			)
			
			# send HTML email to newly registered user
			user.get_profile().send_email(
				'Активация учетной записи на портале mamochkam.com',
				ACTIVATION_MESSAGE['text'](md5hash.hexdigest()),
				ACTIVATION_MESSAGE['html'](md5hash.hexdigest())
			)
				
			return render_to_response('user/register/thanx.html', {
				'email': user.email
			}, context_instance=RequestContext(request))
	
	return render_to_response(
		'user/register/form.html',
		{'form': form},
		context_instance=RequestContext(request)
	)
