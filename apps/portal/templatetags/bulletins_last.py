# -*- coding: utf-8 -*-
from django import template
from mamochkam.apps.bulletins.models import Bulletin

register = template.Library()

@register.inclusion_tag('portal/_last-bulletins.html')
def bulletins_last(count):
	try:
		return { 'bulletins': Bulletin.objects.latest('pub_date').filter(is_news=is_news)[:int(count)] }
	
	except ValueError:
		return { 'bulletins': [] }

