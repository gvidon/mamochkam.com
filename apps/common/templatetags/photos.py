# -*- coding: utf-8 -*-
from django                       import template
from mamochkam.apps.photos.models import Photo

register = template.Library()

#RANDOM PHOTOS
@register.inclusion_tag('portal/_random-photos.html')
def random_photos(count):
	try:
		return { 'photos': Photo.objects.order_by('?')[:int(count)] }
	
	except IndexError:
		return { 'photos': [] }

#LAST PHOTO TAG
@register.inclusion_tag('photos/_last-photo.html')
def last_photo():
	try:
		return { 'photo': Photo.objects.filter(publish=True).order_by('-pub_date')[0] }
	
	except IndexError:
		return { 'photo': {} }

