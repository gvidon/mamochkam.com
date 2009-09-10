# -*- coding: utf-8 -*-
import hashlib, random, httplib, urllib
from PIL import Image

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models     import User
from django.template.context        import RequestContext
from django.shortcuts               import render_to_response
from django.conf                    import settings

from mamochkam.apps.users.forms     import ProfileForm
from mamochkam.apps.users.models    import Profile

#USER PROFILE FORM
@login_required
def form(request):
	profile = Profile.objects.get(user=request.user)
	
	form = ProfileForm(auto_id='%s', initial={
		'id'        : request.user.get_profile().id,
		'username'  : request.user.username,
		'email'     : request.user.email,
		'avatar'    : profile.avatar,
		
		'first_name': request.user.first_name,
		'sur_name'  : profile.sur_name,
		'last_name' : request.user.last_name,
		
		'gender'    : profile.gender,
		'birthdate' : profile.birthdate,
		
		'phone'     : profile.phone,
		'icq'       : profile.icq,
	})
	
	if request.POST:
		form = ProfileForm(auto_id='%s', data=request.POST, files=request.FILES)
		
		if(form.is_valid()):
			
			# update user info and profile
			User(
				id         = request.user.id,
				username   = form.cleaned_data.get('username'),
				email      = form.cleaned_data.get('email'),
				first_name = form.cleaned_data.get('first_name'),
				last_name  = form.cleaned_data.get('last_name')
			).save()
			
			Profile(
				id        = form.cleaned_data.get('id'),
				user      = request.user,
				avatar    = request.FILES and 'upload/avatars/'+request.POST['username'] or '',
				sur_name  = form.cleaned_data.get('sur_name'),
				gender    = form.cleaned_data.get('gender'),
				birthdate = form.cleaned_data.get('birthdate'),
				phone     = form.cleaned_data.get('phone'),
				icq       = form.cleaned_data.get('icq')
			).save()
			
			# resize and save uploaded avatar
			if request.FILES:
				filename = settings.UPLOAD_ROOT+'avatars/'+request.POST['username']
				
				avatar = open(filename,'wb+')
				for chunk in request.FILES['avatar'].chunks(): avatar.write(chunk)
				avatar.close()
				
				image = Image.open(filename)
				
				if image.mode not in ('L', 'RGB'):
					image = image.convert('RGB')
				
				image.thumbnail((100, 100), Image.ANTIALIAS)
				image.save(filename, image.format)
			
	return render_to_response('user/profile.html', {
		'form'   : form,
		'profile': profile,
	}, context_instance=RequestContext(request)
	)
