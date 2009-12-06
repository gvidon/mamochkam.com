# -*- coding: utf-8 -*-
from django.template.defaultfilters  import stringfilter
from django.conf                     import settings
from django                          import template

from mamochkam.apps.pressroom.models import Article, Section
from mamochkam.apps.photos.models    import Gallery
from mamochkam.apps.forum.models     import ThreadComment

# Querysets are executed only when objects are iterated
queryset = {
	'articles': Section.objects.all(),
	'news'    : Section.objects.all(),
	'photos'  : Gallery.objects.all(),
}

register = template.Library()

#ВЫБРАТЬ СТАТЬИ ПО КРИЕТРИЮ
def articles(count, is_news, is_school=None):
	try:
		articles = Article.objects.filter(is_news=is_news, publish=1)
		
		if is_school != None:
			articles = articles.filter(is_school=is_school)
		
		return {'articles': articles.order_by('-pub_date')[:int(count)]}
	
	except ValueError:
		return { 'articles': [] }

#СПИСОК КАТЕГОРИЙ ЧЕГО УГОДНО
@register.inclusion_tag('common/_categories.html')
def categories(type, url):
	try:
		return {
			'categories': queryset[type],
			'url'       : url + '/' + queryset[type][0].__class__.__name__.lower(),
		}
	
	except ValueError:
		return { 'categories': [] }

#ДАЙДЖЕСТ СТАТЕЙ БЕЗ САММАРИ
@register.inclusion_tag('common/_last-articles.html')
def last_articles(count, is_news, is_school=None):
	return { 'articles' : articles(count, is_news, is_school)['articles'], 'is_short': False }

#ДАЙДЖЕСТ СТАТЕЙ С САММАРИ
@register.inclusion_tag('common/_last-articles.html')
def last_articles_short(count, is_news, is_school=None):
	return { 'articles' : articles(count, is_news, is_school)['articles'], 'is_short': True }

#ПОСЛЕДНИЕ СООБЩЕНИЯ ФОРУМА
@register.inclusion_tag('common/_last-messages.html')
def last_messages(count):
	return { 'messages': ThreadComment.objects.order_by('-pub_date')[:int(count)] }
