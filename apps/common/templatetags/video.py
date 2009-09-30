# -*- coding: utf-8 -*-
from django                      import template
from mamochkam.apps.video.models import Video

register = template.Library()

#RANDOM VIDEO
@register.inclusion_tag('video/_random-video.html')
def random_video(count):
	try:
		return { 'video': Video.objects.order_by('?')[:int(count)] }
	
	except IndexError:
		return { 'video': [] }

#LAST VIDEO TAG
@register.inclusion_tag('video/_last-video.html')
def last_video():
	try:
		return { 'video': Video.objects.filter(publish=True).order_by('-pub_date')[0] }
	
	except IndexError:
		return { 'video': {} }

