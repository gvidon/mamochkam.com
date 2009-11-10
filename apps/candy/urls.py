# -*- coding: utf-8 -*-
from django.conf                      import settings
from django.conf.urls.defaults        import *
from django.views.generic.list_detail import object_detail

from mamochkam.apps.candy.models      import Category, Product
from mamochkam.apps.candy.views       import featured, cart, confirm, order, orders, product

urlpatterns = patterns('',
	# главная - топовые товары и лист категорий
	url(r'^$', featured, name='candy'),
	
	#корзина и оформление заказа
	url(r'^cart/?$'                                            , cart   , name='candy-cart'),
	url(r'^order/(?P<id>[0-9]+)/?$'                            , order  , name='candy-order'),
	url(r'^order/(?P<id>[0-9]+)/confirm/?$'                    , confirm, name='candy-confirm'),
	
	url(r'^orders/?$'                                          , orders , name='candy-orders'),
	
	# серфинг по каталогу
	url(r'^(?P<slug>[\w\d\-_]+)/?(page/(?P<page>[0-9]+)/?)?$', object_detail, {
		'slug_field'   : 'slug',
		'paginate_by'  : settings.ITEMS_PER_PAGE,
		'allow_empty'  : True,
		'queryset'     : Category.objects.all(),
		'template_name': 'category.html',
	}, name='candy-category'),
	
	url(r'^(?P<category>[\w\d\-_]+)/(?P<product>[\w\d\-_]+)/?$', product, name='candy-product'),
)

