# -*- coding: utf-8 -*-
from django import template
from mamochkam.apps.pressroom.models import Article

register = template.Library()

@register.inclusion_tag('portal/_last-articles.html')
def articles_last(count, is_news=False):
	try:
		return { 'articles': Article.objects.latest('pub_date').filter(is_news=is_news)[:int(count)] }
	
	except ValueError:
		return { 'articles': [] }

