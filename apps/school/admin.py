from django.contrib               import admin
from mamochkam.apps.school.models import Direction

class DirectionAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'priority')

admin.site.register(Direction, DirectionAdmin)

