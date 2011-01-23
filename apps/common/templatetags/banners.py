# -*- coding: utf-8 -*-
from datetime                     import datetime

from django.conf                  import settings
from django                       import template

from mamochkam.apps.portal.models import Banner, BannerLog

register = template.Library()

@register.simple_tag
def banner(size, ip):
	queryset = Banner.objects.filter(size=size, is_active=True)
	
	try:
		# сначала глянуть постоянные баннеры
		if queryset.filter(is_permanent=True).count():
			banner = queryset.filter(is_permanent=True)[0]
		
		#если постоянных нет - показывать обычные
		else:
			banner = queryset.order_by('?')[0]
		
	except IndexError:
		return ''
		
	# отметиться в логах если этот IP еще не смотрел баннер
	if not banner.log.filter(ip=ip).count():
		banner.log.create(ip=ip)
		banner.counter += 1
	
	# проверить активность по временному и каунт пределам
	banner.is_active = (banner.counter < banner.limit) or ((banner.date_limit or datetime.today()) >= datetime.today())
	banner.save()
	
	return '<a href="/advert-redirect/'+str(banner.id)+'"><img src="'+banner.image.url+'" /></a>' 
