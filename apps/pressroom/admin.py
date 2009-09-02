from django.contrib                  import admin
from mamochkam.apps.pressroom.models import Article, Section

class ArticleAdmin(admin.ModelAdmin):
	pass
	
class SectionAdmin(admin.ModelAdmin):
	pass

admin.site.register(Article, ArticleAdmin)
admin.site.register(Section, SectionAdmin)

