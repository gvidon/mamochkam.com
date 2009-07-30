# -*- coding: utf-8 -*-
from django.template.defaultfilters  import stringfilter
from django.conf                     import settings
from django                          import template

from mamochkam.apps.pressroom.models import Article, Section
from mamochkam.apps.photos.models    import Gallery

# Querysets are executed only when objects are iterated
queryset = {
	'articles': Section.objects.all(),
	'news'    : Section.objects.all(),
	'photos'  : Gallery.objects.all(),
}

register = template.Library()

@register.inclusion_tag('common/_last-articles.html')
def last_articles(count, is_news):
	try:
		return {
			'articles': Article.objects.filter(is_news=is_news, publish=1).order_by('-pub_date')[:int(count)]
		}
	
	except ValueError:
		return { 'articles': [] }

@register.inclusion_tag('common/_categories.html')
def categories(type, url):
	try:
		return {
			'categories': queryset[type],
			'url'       : url + '/' + queryset[type][0].__class__.__name__.lower(),
		}
	
	except ValueError:
		return { 'categories': [] }
