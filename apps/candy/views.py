# -*- coding: utf-8 -*-
from datetime                       import datetime

from django.contrib.auth.decorators import login_required
from django.template.context        import RequestContext
from django.core.exceptions         import ValidationError
from django.views.generic           import list_detail
from django.shortcuts               import render_to_response
from django.shortcuts               import get_object_or_404
from django.conf                    import settings
from django.http                    import HttpResponse

from models                         import Product

#ОБЗОР ЗАКАЗАННЫХ АЙТЕМОВ
def cart(request):
	return HttpResponse('1')

#ПРОЦЕДУРА ПОДТВЕРЖДЕНИЯ ДАННЫХ ЗАКАЗА
def confirm(request):
	return HttpResponse('1')

#СТРАНИЦА ТОПОВЫХ ТОВАРОВ
def featured(request):
	return render_to_response('candy/featured.html', {
		'featured_items': Product.objects.filter(is_featured=True).order_by('?')
	}, context_instance=RequestContext(request))

#ОБЗОР УСЛОВИЙ ЗАКАЗА И КОММЕНТАРИИ К НЕМУ
def order(request):
	return HttpResponse('1')

#СПИСОК УЖЕ СОВЕРШЕННЫХ ЗАКАЗОВ
def orders(request):
	return HttpResponse('1')

#СТРАНИЦА ПРОДУКТА
def product(request, category, product):
	return render_to_response('candy/product.html', {
		'product': get_object_or_404(Product, category__slug=category, slug=product)
	}, context_instance=RequestContext(request))
