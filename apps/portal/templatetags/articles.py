# -*- coding: utf-8 -*-
from django.template.defaultfilters  import stringfilter
from django                          import template
from mamochkam.apps.pressroom.models import Article

register = template.Library()

@register.inclusion_tag('portal/_last-articles.html')
def articles(count, is_news):
	try:
		return {
			'articles': Article.objects.filter(is_news=is_news, publish=1).order_by('-pub_date')[:int(count)]
		}
	
	except ValueError:
		return { 'articles': [] }
