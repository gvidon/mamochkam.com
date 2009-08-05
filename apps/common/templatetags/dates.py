# -*- coding: utf-8 -*-
from datetime                        import date
from mamochkam.apps.pressroom.models import Article
from django.template.defaultfilters  import stringfilter
from django                          import template

# Attach 3 characters month name to the list
months = [month + [month[0][0:3]] for month in [
	[ 'January'  , u'Январь'  , u'Января'   ],
	[ 'February' , u'Февраль' , u'Февраля'  ],
	[ 'March'    , u'Март'    , u'Марта'    ],
	[ 'April'    , u'Апрель'  , u'Апреля'   ],
	[ 'May'      , u'Май'     , u'Мая'      ],
	[ 'June'     , u'Июнь'    , u'Июня'     ],
	[ 'July'     , u'Июль'    , u'Июля'     ],
	[ 'August'   , u'Август'  , u'Августа'  ],
	[ 'September', u'Сентябрь', u'Сентября' ],
	[ 'October'  , u'Октябрь' , u'Октября'  ],
	[ 'November' , u'Ноябрь'  , u'Ноября'   ],
	[ 'December' , u'Декабрь' , u'Декабря'  ],
]]


register = template.Library()

#ALL MONTHES LIST SINCE FIRST ITEM PUB DATE
@register.inclusion_tag('common/_full-archive.html')
def full_archive(url):
	year = date.today().year
	
	return {
		'url'        : url,
		'months'     : months,
		
		'past_years' : [year for year in range(
			Article.objects.exclude(pub_date=None).order_by('pub_date')[0].pub_date.year, date.today().year - 1
		)],
	}

#TRANSLATE ENG MONTH NAMES
@register.filter(name='ru_months')
@stringfilter
def ru_months(date):
	try:
		return [
			date.replace(month[0], month[2]) for month in months if date.find(month[0]) != -1
		][0]
	
	except IndexError:
		return ''

#THIS YEAR PAST MONTHES
@register.inclusion_tag('common/_year-months.html')
def this_year_months(url):
	for today in [date.today()]:
		return {
			'url'   : url,
			'year'  : today.year,
			'months': months[0:today.month],
		}
