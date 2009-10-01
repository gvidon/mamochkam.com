from django.contrib                  import admin
from mamochkam.apps.pressroom.models import ArticleComment, Article, Section

class ArticleCommentAdmin(admin.ModelAdmin):
	pass
	
class ArticleAdmin(admin.ModelAdmin):
	pass
	
class SectionAdmin(admin.ModelAdmin):
	pass

admin.site.register(ArticleComment, ArticleCommentAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Section, SectionAdmin)

