# -*- coding: utf-8 -*-
from django.template.defaultfilters  import stringfilter
from django                          import template
from mamochkam.apps.pressroom.models import Article

register = template.Library()

@register.filter(name='ru_monthes')
@stringfilter
def ru_monthes(date):
	monthes = {
		'January'  : u'Января',
		'February' : u'Февраля',
		'March'    : u'Марта',
		'April'    : u'Апреля',
		'May'      : u'Мая',
		'June'     : u'Июня',
		'July'     : u'Июля',
		'August'   : u'Августа',
		'September': u'Сентября',
		'October'  : u'Октября',
		'November' : u'Ноября',
		'December' : u'Декабря',
	}
	
	for eng, ru in monthes.iteritems():
		ru_date = date.replace(eng, ru)
	
	return ru_date
