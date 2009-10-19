from django.contrib                  import admin
from mamochkam.apps.pressroom.models import ArticleComment, Article, Section

class ArticleCommentAdmin(admin.ModelAdmin):
	pass
	
class ArticleAdmin(admin.ModelAdmin):
	list_display = ('headline', 'pub_date', 'is_news', 'is_school')
	
class SectionAdmin(admin.ModelAdmin):
	pass

admin.site.register(ArticleComment, ArticleCommentAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Section, SectionAdmin)

