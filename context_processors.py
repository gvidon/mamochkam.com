from django.conf import settings

#SEPARATE MEDIA SERVER URL
def media_url(request):
	return { 'media_url': settings.MEDIA_URL }
