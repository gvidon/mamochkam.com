from django.conf import settings
#from workspace.profile.models import Profile

#SEPARATE MEDIA SERVER URL
def media_url(request):
	return { 'media_url': settings.MEDIA_URL }

#PROVIDE PROFILE DATA IN TEMPLATE
'''
def profile(request):
	try:
		return { 'profile': Profile.objects.get(user=request.user) }
	except Profile.DoesNotExist:
		return { 'profile': {} }
'''
