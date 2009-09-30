from django.contrib               import admin
from mamochkam.apps.portal.models import Banner, BannerLog

class BannerAdmin(admin.ModelAdmin):
	list_display = (lambda obj: obj.image.url, 'size', 'counter', 'limit', 'date_limit', 'is_active')
	
class BannerLogAdmin(admin.ModelAdmin):
	list_display = ('ip', 'created_at')

admin.site.register(BannerLog, BannerLogAdmin)
admin.site.register(Banner, BannerAdmin)

