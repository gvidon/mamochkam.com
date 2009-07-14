# -*- coding: utf-8 -*-
from django import template
from mamochkam.apps.tags.models import Tag

register = template.Library()

@register.inclusion_tag('portal/_top-tags.html')
def tags_top(count):
	try:
		return {'tags': [{
			'title': title,
			'count': Tag.objects.filter(title=title).count()
		} for title in set([tag.title for tag in Tag.objects.order_by('?').distinct()])]}
	
	except ValueError:
		return { 'tags': [] }

