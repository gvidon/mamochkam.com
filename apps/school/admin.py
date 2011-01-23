from mamochkam.apps.school.models import Direction
from django.contrib               import admin
from django.conf                  import settings

class DirectionAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'priority')
	
	class Media:
		css = { 'all': (settings.MEDIA_URL+'/css/rte.css',) }
		
		js = (
			settings.MEDIA_URL+'/js/lib/jquery.min.js',
			settings.MEDIA_URL+'/js/lib/jquery.rte.js',
			settings.MEDIA_URL+'/js/admin/wysiwyg.js',
		)

admin.site.register(Direction, DirectionAdmin)

