# -*- coding: utf-8 -*-
from django.contrib               import admin
from mamochkam.apps.portal.models import Banner, BannerLog

class BannerAdmin(admin.ModelAdmin):
	exclude      = ('counter',)
	list_display = (lambda obj: obj.image.url, 'size', 'counter', 'limit', 'date_limit', 'is_active')
	
	list_display[0].short_description = u'Изображение'
	
class BannerLogAdmin(admin.ModelAdmin):
	list_display = ('ip', 'created_at')

admin.site.register(BannerLog, BannerLogAdmin)
admin.site.register(Banner, BannerAdmin)

