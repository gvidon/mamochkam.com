from django.contrib               import admin
from mamochkam.apps.search.models import Tag

class TagAdmin(admin.ModelAdmin):
	pass

admin.site.register(Tag, TagAdmin)

