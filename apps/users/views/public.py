# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models     import User
from django.template.context        import RequestContext
from django.shortcuts               import render_to_response
from django.conf                    import settings
from django.http                    import Http404

from mamochkam.apps.users.forms     import ProfileForm
from mamochkam.apps.users.models    import Profile

def profile(request, username):
	try:
		return render_to_response('user/public/profile.html', {
			'user': User.objects.get(username=username)
		}, context_instance=RequestContext(request))
			
	except:
		raise Http404
