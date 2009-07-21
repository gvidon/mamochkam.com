# -*- coding: utf-8 -*-
from django                       import template
from mamochkam.apps.photos.models import Photo

register = template.Library()

@register.inclusion_tag('portal/_random-photos.html')
def random_photos(count):
	try:
		return { 'photos'   : Photo.objects.order_by('?')[:int(count)] }
	
	except ValueError:
		return { 'photos': [] }

