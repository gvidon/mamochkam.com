# -*- coding: utf-8 -*-
from django                          import template
from mamochkam.apps.bulletins.models import Bulletin

register = template.Library()

@register.inclusion_tag('common/_last-bulletins.html')
def last_bulletins(count):
	try:
		return { 'bulletins': Bulletin.objects.filter(publish=1).order_by('-pub_date')[:int(count)] }
	
	except ValueError:
		return { 'bulletins': [] }

