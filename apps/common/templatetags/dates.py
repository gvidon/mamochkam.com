# -*- coding: utf-8 -*-
from datetime                        import date
from mamochkam.apps.pressroom.models import Article
from django.template.defaultfilters  import stringfilter
from django                          import template

months = {
	'January'  : [ u'Январь'  , u'Января' ],
	'February' : [ u'Февраль' , u'Февраля' ],
	'March'    : [ u'Март'    , u'Марта' ],
	'April'    : [ u'Апрель'  , u'Апреля' ],
	'May'      : [ u'Май'     , u'Мая' ],
	'June'     : [ u'Июня'    , u'Июня' ],
	'July'     : [ u'Июль'    , u'Июля' ],
	'August'   : [ u'Август'  , u'Августа'],
	'September': [ u'Сентябрь', u'Сентября' ],
	'October'  : [ u'Октябрь' , u'Октября'],
	'November' : [ u'Ноябрь'  , u'Ноября'],
	'December' : [ u'Декабрь' , u'Декабря'],
}
	
register = template.Library()

@register.filter(name='ru_months')
@stringfilter
def ru_months(date):

	for eng, ru in months.iteritems():
		ru_date = date.replace(eng, ru[1])
	
	return ru_date

@register.inclusion_tag('common/_year-months.html')
def this_year_months(url):
	for today in [date.today()]:
		return {
			'year'  : today.year,
			'url'   : url,
			
			'months': [[
				months[date(today.year, i, 1).strftime('%B')][0], date(today.year, i, 1).strftime('%b')
			] for i in range(1, today.month + 1)],
		}
	
	
	
